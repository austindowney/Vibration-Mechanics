

% Time span for simulation
tspan = [0, 10]; % Start time and end time

% Initial conditions [x1, x1', x2, x2']
initial_conditions = [0, 0, 0, 0];

% Use ode45 to solve the system of ODEs
[t, y] = ode45(@equations_of_motion, tspan, initial_conditions);

% Extract displacements of masses
x1 = y(:, 1);
x2 = y(:, 2);

% Plot the displacement responses
figure;
plot(t, x1, '-', 'LineWidth', 1.2);
hold on;
plot(t, x2, '--', 'LineWidth', 1.2);
legend('Mass 1', 'Mass 2');
xlabel('time (s)');
ylabel('displacement (m)');
%title('Displacement response of the 1-DOF system');
grid on;
f = gcf;
exportgraphics(f,'ODE_results-2-DOF.jpg','Resolution',300)


% Equations of motion for the system
function [dydt,F_t] = equations_of_motion(t, y)

% Setup the system parameters
m1=2; m2=1; k1=20; k2=10; c1=0.5; c2=1;

% Build the Mass, Damping, and Stiffnes matrices 
M = [m1, 0; 0, m2];
C = [c1 + c2, -c2; -c2, c2];
K = [k1 + k2, -k2; -k2, k2];

% Unpack the state variables
x = y(1:2);
x_dot = y(3:4);

% Define the force excitation vector F(t) here
% Replace 'force_excitation_vector(t)' with your actual force excitation vector
F_t = force_excitation_vector(t);



% Equations of motion
x_dotdot = inv(M) * (F_t - C * x_dot - K * x);

% Pack the derivatives into the output vector dydt
dydt = [x_dot; x_dotdot];
end

% Define the force excitation vector F(t) here
function F_t = force_excitation_vector(t)

if t<1 % Ramp load from 0 to 1 second 
    f1_t = t;
else % constant load after 1 second 
    f1_t=1;
end

F_t = [f1_t; 0]; % force vector, no load on f2

end
