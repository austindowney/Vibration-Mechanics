clear
close
clc


m_1 = 10    % kg
m_2 = 1     % kg
k_1 = 30    % N/m
k_2 = 5    % N/m
k_3 = 1    % N/m
x_1_0 = 1 % m
x_2_0 = 0 % mm
v_1_0 = 0 % mm
v_2_0 = 0 % mm

tt = linspace(0,20,1000)

M = zeros(2,2)
M(1,1)= m_1
M(2,2)= m_2


K = zeros(2,2)
K(1,1)= k_1+k_2
K(1,2)= -k_2
K(2,1)= -k_2
K(2,2)= k_2+k_3




% solve the generlized eignevalue problem
[eig_vect,eig_value]=eig(K,M)

v_1 =  eig_vect(:,1)
v_2 =  eig_vect(:,2)


% convert the the standard form
M_inv_sqrt = inv(sqrt(M))
K_mass_norm = M_inv_sqrt*K*M_inv_sqrt
[eig_vect_2,eig_value_2]=eig(K_mass_norm)
%v_1 =  np.round(eig_vect[:,0]/eig_vect[0,0])
%v_2 =  np.round(eig_vect[:,1]/eig_vect[0,0])
