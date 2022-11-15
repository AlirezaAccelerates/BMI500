% BMI500 HW12 - Motion Analysis 1
% Modified by: Alireza Rafiei

% reset the workspace
clear
close all

% load spiral drawing data
d = read_trc("lue-spiral.trc");

% set plotting parameters
TL = [0 5];
nr = 2;
nc = 3;

% plot the left hand marker in x-y-z
marker_name = "L.Finger3.M3";
marker_xyz = d{:,find(names(d) == "L.Finger3.M3") + [0:2]};

t = d{:,"Time"};
t_inds = t>min(TL)&t<max(TL);
t_secs = rem(t(t_inds),1)==0;


% plot
figure
subplot(nr,nc,1)
hold on

%%% Plot the X, Y, Z data of the L.Finger3.M3 marker
plot(t, marker_xyz(:,1))
plot(t, marker_xyz(:,2))
plot(t, marker_xyz(:,3))
title('Raw Data')
xlabel('seconds')
ylabel('mm')
legend('X','Y','Z')
xlim([0 5])
ylim([0 1400])
hold off

subplot(nr,nc,2)
hold on
plot(marker_xyz(:,2),marker_xyz(:,3),'k');
title('Front View')
xlabel('Y')
ylabel('Z')
ylim([800 1300])
xlim([0 300])
hold off

% Filter out large, slow movements with a high-pass butterworth filter at 2
% Hz cutoff and filter out jitter with a low-pass butterworth filter at 20
% Hz cutoff. A 6th order filter is fine.

% sampling freq fs is the reciprocal of the difference between two points
fs = 1/mean(diff(t));

% cutoff frequencies for the filter
fc_hi = 2;
fc_lo = 20;

% [b,a] = butter(n,Wn) returns the transfer function coefficients of an 
% nth-order lowpass digital Butterworth filter with normalized 
% cutoff frequency Wn [https://www.mathworks.com/help/signal/ref/butter.html]

%%% Filter the original dat two ways.
[b,a] = butter(6, [fc_hi/(fs/2) fc_lo/(fs/2)]);
marker_filter = filtfilt(b,a,marker_xyz);

[b2,a2] = butter(6,fc_hi/(fs/2));
marker_lowfilt = filtfilt(b2,a2,marker_xyz);

subplot(nr,nc,3)
hold on
plot(marker_lowfilt(:,2),marker_lowfilt(:,3),'k');
title('Low Frequency Componet')
xlabel('Y')
ylabel('Z')
ylim([800 1300])
xlim([0 300])
hold off

%%% Calculate and plot the first PC
[coeff,score,latent] = pca(marker_filter);
first_pc = score(:,1)*coeff(:,1)';

subplot(nr,nc,4)
hold on
plot(marker_filter(:,2),marker_filter(:,3),'k');
plot(first_pc(:,2),first_pc(:,3));
title('High frequency componet and 1st PC')
xlabel('Y')
ylabel('Z')
xlim([-75 75])
ylim([-50 50])
hold off

%%% Calculate projection onto first PC
proj = marker_filter*coeff(:,1);

% smooth with a savitsky-golay smoother
proj_smooth = smoothdata(proj,'sgolay');

% count zero crossings
zcd = dsp.ZeroCrossingDetector();
numZeroCross = cast(zcd(proj_smooth(t_inds)),"double");
tremorFrequency = (numZeroCross/2)/max(TL);

% get envelope from 25 sample moving average
env_width = 25;
env = movmax(proj_smooth(t_inds),env_width);

% use the median of the moving maximum as the estimator of the amplitude
amp = median(env);

ttl = round(tremorFrequency,1) + " Hz, " + round(2*amp,1) + " mm amplitude";

% plot
subplot(nr,nc,[5 6])
hold on
plot(t,proj,'k.')
plot(t,proj_smooth,'r')
h1 = refline(0,amp);
h2 = refline(0,-amp);
h1.Color = 0.5*[1 1 1];
h2.Color = 0.5*[1 1 1];
xlim(TL)
title(ttl)
ylabel("mm")
xlabel("seconds")