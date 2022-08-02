function f = matlab_function_dfunc(t,y)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
f=zeros(4,1)
f(1) = y(2)
f(2) = cos(3*t) - 4*y(2) + y(4) - 5*y(1) + 2*y(3)
f(3) = y(2)
f(4) = cos(3*t) + 0.5*y(2) - y(4) + y(1) - 1.5*y(3)
end
