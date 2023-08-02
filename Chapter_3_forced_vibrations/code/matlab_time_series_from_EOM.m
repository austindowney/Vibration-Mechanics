clear
close 
clc


% Time span for simulation
tspan = [0, 10]; % Start time and end time

% Initial conditions [x, x']
initial_conditions = [0, 0];

% Use ode45 to solve the system of ODEs
[t, y] = ode45(@equation_of_motion, tspan, initial_conditions);

% Extract displacement and velocity
x = y(:, 1);
x_dot = y(:, 2);

% Plot the displacement response
figure;
plot(t, x, 'b-', 'LineWidth', 2);
xlabel('time (s)');
ylabel('displacement (m)');
%title('Displacement response of the 1-DOF system');
grid on;
f = gcf;
exportgraphics(f,'ODE_results.jpg','Resolution',300)


% Equation of motion for the system
function dydt = equation_of_motion(t, y)

    % Mass, damping coefficient, and spring constant
    m = 1.0; % Mass
    c = 0.2; % Damping coefficient
    k = 2.0; % Spring constant

    % Unpack the state variables
    x = y(1);
    x_dot = y(2);

    % Define the force excitation function f(t) here
    % Replace 'force_excitation_function(t)' with your actual force excitation function
    f_t = force_excitation_function(t);

    % Equation of motion
    x_dotdot = (f_t - c * x_dot - k * x) / m;

    % Pack the derivatives into the output vector dydt
    dydt = [x_dot; x_dotdot];
end

% Define the force excitation function f(t) here
% Replace 'force_excitation_function(t)' with your actual force excitation function
function f_t = force_excitation_function(t)
    % Example: A simple sinusoidal force excitation
    % Replace this with your own function or any other excitation pattern you want to simulate
    f_t = 0.5 * sin(2 * pi * t);
end





