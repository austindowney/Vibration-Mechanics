clear
close 
clc

% example 5.15
% eigenvalue
% A = [2 -1; -1 2]
% [V,D] = eig(A)
% 
% example 5.16
% for the function f(x) = x^4 -8x +12 =0
% roots([1 0 0 -8 12]) 
% 
% example 5.20





tspan = [0: 0.1 : 20]
y0 = [0.2; 1.0; 0.0; 8.0];
[t,y] = ode23('dfunc5_15',tspan, y0)

figure()
subplot(211)
plot(t,y(:,1))
xlabel('time (s)')
ylabel('x1(t) (m)')
subplot(212)
plot(t,y(:,3))
xlabel('time (s)')
ylabel('x1(t) (m)')





