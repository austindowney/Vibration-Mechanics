% Generalized eigenvalue solution for a 9-DOF wing model
clear; clc;

% ---- Define lumped masses (kg), left tip -> right tip ----
m = [45,60,120,60,420,60,120,60,45]';    % m1,m2,m3,m2,m4,...
n = numel(m);                            % number of DOF
M = diag(m);                             % mass matrix

% ---- Define stiffness parameter ----
l = 1.8;  E = 70e9;  I = 8.0e-5;          % geometry & material
k = 3*E*I/l^3;                           % element stiffness

% ---- Assemble global stiffness matrix ----
K = zeros(n);
for i = 1:n-1
    K(i,i)     = K(i,i)     + k;
    K(i+1,i+1) = K(i+1,i+1) + k;
    K(i,i+1)   = K(i,i+1)   - k;
    K(i+1,i)   = K(i+1,i)   - k;
end

% ---- Solve generalized eigenvalue problem ----
% K*v = lambda*M*v
[V,L] = eig(K,M);                        % eigenvectors & eigenvalues
lambda = diag(L);                        % extract eigenvalues

% ---- Sort modes by increasing frequency ----
[lambda,idx] = sort(lambda);
V = V(:,idx);

% ---- Compute natural frequencies ----
omega = sqrt(max(lambda,0));             % rad/s
f = omega/(2*pi);                        % Hz

% ---- Mass-normalize mode shapes ----
for j = 1:n
    V(:,j) = V(:,j)/sqrt(V(:,j)'*M*V(:,j));
end

% ---- Display results ----
fprintf('First five natural frequencies (Hz):\n');
disp(f(1:5))

fprintf('First mode shape (mass-normalized):\n');
disp(V(:,1))
