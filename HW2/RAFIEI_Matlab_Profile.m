profile on

% Mesh data
x=0.01;
M=11;
N=21;
P=800;

% Initial values of the problem
Ts=140;
h=80;
k=15;
a=3.2*10^(-6);
qdot=2*10^7;
qs=8000;
Tinf=25;
Fo=0.25;
t=Fo*(x^2)/a;
A=a*t/(x^2);
B=2*a*t/(k*x);
C=t*a/k;
D=2*h*a*t/(k*x);

T=zeros(M,N,2);
T(:,:,1)=Ts;
X(P)=0;
Y1(P)=0;
Y2(P)=0;
Y3(P)=0;
Y4(P)=0;
Y5(P)=0;
Y6(P)=0;
Y7(P)=0;
Y8(P)=0;


% Explicit method
for p=1:P
   for m=1:M
       for n=1:N
           if m>1 && m<M && n>1 && n<N
              T(m,n,p+1)=A*( T(m-1,n,p)+T(m,n+1,p)+T(m+1,n,p)+T(m,n-1,p)-4*T(m,n,p) ) + C*qdot + T(m,n,p);
           end
           if m>1 && m<M && n==1
              T(m,1,p+1)=A*( T(m-1,1,p)+2*T(m,2,p)+T(m+1,1,p)-4*T(m,1,p) ) + B*qs + C*qdot + T(m,1,p);
           end
           if m==1 && n>1 && n<N
              T(1,n,p+1)=D*(Tinf-T(1,n,p)) + A*( T(1,n+1,p)+2*T(2,n,p)+T(1,n-1,p)-4*T(1,n,p) ) + C*qdot + T(1,n,p);
           end
           if m==1 && n==1
              T(1,1,p+1)=D*(Tinf-T(1,1,p)) + 2*A*( T(1,2,p)+T(2,1,p)-2*T(1,1,p) ) + B*qs + C*qdot + T(1,1,p); 
           end
           if m>1 && m<M && n==N
              T(m,N,p+1)=A*( T(m-1,N,p)+2*T(m,N-1,p)+T(m+1,N,p)-4*T(m,N,p) ) + C*qdot + T(m,N,p);
           end
           if m==1 && n==N
              T(1,N,p+1)=D*(Tinf-T(1,N,p)) + 2*A*( T(1,N-1,p)+T(2,N,p)-2*T(1,N,p) ) + C*qdot + T(1,N,p);
           end
           if m==M
              T(M,n,p+1)=Ts;
           end
       end
   end
   X(p)=p;
   Y1(p)=T(ceil(1*M/11),ceil(21*N/21),p);
   Y2(p)=T(ceil(3*M/11),ceil(10*N/21),p);
   Y3(p)=T(ceil(5*M/11),ceil(15*N/21),p);
   Y4(p)=T(ceil(5*M/11),ceil(19*N/21),p);
   Y5(p)=T(ceil(10*M/11),ceil(20*N/21),p);
   Y6(p)=T(ceil(10*M/11),ceil(8*N/21),p);
   Y7(p)=T(ceil(10*M/11),ceil(10*N/21),p);
   Y8(p)=T(ceil(8*M/11),ceil(15*N/21),p);
end
plot(X,Y1,X,Y2,X,Y3,X,Y4,X,Y5,X,Y6,X,Y7,X,Y8);

% Mirroring matrix T
T_=T;
for p=1:P
   for m=1:(floor(M/2))
       for n=1:N
           temp = T_(m,n,p);
           T_(m,n,p) = T_(M+1-m,n,p);
           T_(M+1-m,n,p) = temp;
       end
   end
end

% Prepare the output for Tecplot
% 10 times before steady state
R(M*N,12)=0;
i=1;
for m=1:M
    for n=1:N
           R(i,1) = (n-1)*x*100;
           R(i,2) = (m-1)*x*100;
           R(i,3) = T_(m,n,0.1*P);
           R(i,4) = T_(m,n,0.2*P);
           R(i,5) = T_(m,n,0.3*P);
           R(i,6) = T_(m,n,0.4*P);
           R(i,7) = T_(m,n,0.5*P);
           R(i,8) = T_(m,n,0.6*P);
           R(i,9) = T_(m,n,0.7*P);
           R(i,10) = T_(m,n,0.8*P);
           R(i,11) = T_(m,n,0.9*P);
           R(i,12) = T_(m,n,P);
           i=i+1;
    end
end
dlmwrite('HT_PRO.txt',R,'delimiter','\t');
%disp(T);

% Temperature distribution in left side
LS(M)=0;
Tls(M)=0;
for m=1:M
    LS(m)=(m-1)*x*100;
    Tls(m)=T_(m,1,P);
end

% Changes in heat flux in up side
US(N)=0;
Qus(N)=0;
for n=1:N
    US(n)=(n-1)*x*100;
    Qus(n)=(-k/x)*( T_(1,n,P)-T_(2,n,P) );
end

% Changes in heat flux in down side
DS(N)=0;
Qds(N)=0;
for n=1:N
    DS(n)=(n-1)*x*100;
    Qds(n)=(-k/x)*( T_(M,n,P)-T_(M-1,n,P) );
end

% Changes in heat flux in right side
RS(M)=0;
Qrs(M)=0;
for m=1:M
    RS(m)=(m-1)*x*100;
    Qrs(m)=(-k/x)*( T_(m,N,P)-T_(m,N-1,P) );
end

figure

subplot(3,4,[2,3]);
plot(US,Qus);
title('Changes in heat flux in up side')
ylabel('Heat flux');
xlabel('X up');

subplot(3,4,5);
plot(Tls,LS);
title('Temperature distribution in left side')
xlabel('Temperature');
ylabel('Y left');

subplot(3,4,8);
plot(Qrs,RS);
title('Changes in heat flux in right side')
xlabel('Heat flux');
ylabel('Y right');

subplot(3,4,[10,11]);
plot(DS,Qds);
title('Changes in heat flux in down side')
ylabel('Heat flux');
xlabel('X down');

profile viewer
p = profile('info')