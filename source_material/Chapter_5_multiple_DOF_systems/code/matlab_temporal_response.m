clear
close 
clc

% define the time stamps of the system
tspan = [0: 0.1 : 20]

% define the initial conditions
y0 = [0.2; 1.0; 0.0; 8.0];

% solge the 2-DOF system using a ODE solver
[t,y] = ode23('matlab_function_dfunc',tspan, y0)

% plot the results
figure()
subplot(211)
plot(t,y(:,1))
xlabel('time (s)')
ylabel('x1(t) (m)')
subplot(212)
plot(t,y(:,3))
xlabel('time (s)')
ylabel('x1(t) (m)')








