clear
close 
clc

% define the M and K matirx
M = [9 0; 0 1]
K = [24+3 -3; -3 3]

% build the M inverse squareroot and mass normalized stiffness matrix 
M_inv_sqr = sqrt(inv(M))
K_mass_norm = M_inv_sqr*K*M_inv_sqr

% Using, K_mass_norm*v=lambda*v
[v,lambda] = eig(K_mass_norm)

% Solve for natural frequencies
omega_1 = sqrt(lambda(1,1))
omega_2 = sqrt(lambda(2,2))

% solve for the mode shapes
u_1 = M_inv_sqr*v(:,1)
u_2 = M_inv_sqr*v(:,2)

% normalize the mode shapes
u_1 = u_1/max(abs(u_1))
u_2 = u_2/max(abs(u_2))








