clear; close all; clc;


%% ---- Parameters (match Table X) ----
l  = 1.8;           % m
E  = 70e9;          % Pa
I  = 8.0e-5;        % m^4
k  = 3*E*I / l^3;   % elemental stiffness (pedagogical estimate)

% mass classes (kg)
m1 = 45;    % tip tank (left/right)
m2 = 60;    % intermediate wing
m3 = 120;   % engine / inner-wing
m4 = 420;   % fuselage center

% mass vector left-tip -> right-tip (9 DOF)
m_vec = [m1, m2, m3, m2, m4, m2, m3, m2, m1]';

%% ---- Build Mass matrix ----
n = length(m_vec);        % should be 9
M = diag(m_vec);          % diagonal mass matrix

%% ---- Build global stiffness matrix for 1D chain ----
K = zeros(n);
for i = 1:(n-1)
    K(i,i)     = K(i,i)     + k;
    K(i+1,i+1) = K(i+1,i+1) + k;
    K(i,i+1)   = K(i,i+1)   - k;
    K(i+1,i)   = K(i+1,i)   - k;
end

%% ---- Solve generalized eigenvalue problem ----
% K*Phi = Lambda*M*Phi
[Phi, Lambda] = eig(K, M);            % Phi columns are eigenvectors
lambda_vals   = diag(Lambda);

% Guard against small negative numerical values
lambda_vals(lambda_vals < 0 & lambda_vals > -1e-12) = 0;

% Sort eigenvalues (and eigenvectors) ascending
[lambda_sorted, idx] = sort(lambda_vals);
Phi_sorted = Phi(:, idx);

% Natural frequencies
omega = sqrt(lambda_sorted);          % rad/s
freq_hz = omega / (2*pi);             % Hz

fprintf('Natural frequencies (Hz):\n');
disp(freq_hz(:))

%% ---- Mass-normalize modes (Phi_nm' * M * Phi_nm = I) ----
Phi_nm = Phi_sorted;                  % copy
for i = 1:size(Phi_nm,2)
    modal_mass = Phi_nm(:,i)' * M * Phi_nm(:,i);   % scalar
    Phi_nm(:,i) = Phi_nm(:,i) / sqrt(modal_mass);
end
% Sanity check (should be identity)
% cond_check = norm(Phi_nm' * M * Phi_nm - eye(n)); disp(cond_check);

%% ---- Prepare mode shapes for plotting (normalize each to max abs = 1) ----
% We'll use the mass-normalized vectors for correctness, then scale for plotting
Phi_plot = Phi_nm;
for i = 1:size(Phi_plot,2)
    Phi_plot(:,i) = Phi_plot(:,i) / max(abs(Phi_plot(:,i)));
end

% Extract first 5 modes for plotting
phi1 = Phi_plot(:,1);
phi2 = Phi_plot(:,2);
phi3 = Phi_plot(:,3);
phi4 = Phi_plot(:,4);
phi5 = Phi_plot(:,5);
phi6 = Phi_plot(:,6);

nodes = 1:n;

%% ---- Plot all five mode shapes in a single figure (no loops) ----
fig = figure('Units','inches','Position',[1 1 6 2.5]);

plot(nodes, phi1, 'o-', 'LineWidth', 1.4, 'MarkerSize', 4); hold on
plot(nodes, phi2, 's--', 'LineWidth', 1.4, 'MarkerSize', 4)
plot(nodes, phi3, 'd-.', 'LineWidth', 1.4, 'MarkerSize', 4)
plot(nodes, phi4, 'v-', 'LineWidth', 1.4, 'MarkerSize', 4)
plot(nodes, phi5, 'p--', 'LineWidth', 1.4, 'MarkerSize', 4)

hold off

grid on
xlabel('node index (1 = left tip, 5 = fuselage center, 9 = right tip)')
ylabel('normalized displacement')

lgd = legend( ...
    sprintf('mode 1 (%.2f Hz)', freq_hz(1)), ...
    sprintf('mode 2 (%.2f Hz)', freq_hz(2)), ...
    sprintf('mode 3 (%.2f Hz)', freq_hz(3)), ...
    sprintf('mode 4 (%.2f Hz)', freq_hz(4)), ...
    sprintf('mode 5 (%.2f Hz)', freq_hz(5)), ...
    'NumColumns',3, ...
    'Orientation','horizontal');


% Shrink axes to make room at top
ax = gca;
ax.Units = 'normalized';
ax.Position = [0.10 0.18 0.85 0.62];   % [left bottom width height]

% Place legend above axes (inside figure)
lgd.Units = 'normalized';
lgd.Position = [0.15 0.82 0.70 0.12];  % centered at top

lgd.Box = 'on';

xlim([1 n])
ylim([-1.2 1.2])


%% ---- Save figure to PNG with exact size ----
% ensure printed size matches figure dimensions
set(gcf,'PaperUnits','inches','PaperPosition',[0 0 6 2.5])
print(gcf, 'N310GMU_mode_shapes', '-dpng', '-r300')