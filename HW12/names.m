function nms = names(d)
% function nms = names(d)
% 
% returns a string vector containing the variable names of table d.

nms = string(d.Properties.VariableNames)';
end