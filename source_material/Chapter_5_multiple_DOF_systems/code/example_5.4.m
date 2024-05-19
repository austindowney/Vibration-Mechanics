clear
close all
clc

% Code for example 5.4, with the question

%{
Consider the system presented in example \ref{ex:2-DOF} and repeated below
where $m_1$=9 kg, $m_2$=1 kg, $k_1$ = 24 N/m, and $k_2$ = 3 N/m with the
initial conditions $x_{10}=1$ mm, $v_{10}=0$ mm/s, $x_{20}=0$ mm, and
$v_{20}=0$ mm/s. Calculate the natural frequencies and the mode shapes
using the eigenvalue solution. 
%}


M = [9 0; 0 1];
K = [27 -3; -3 3];

M_inv_sqr = sqrt(inv(M));
K_equ = M_inv_sqr*K*M_inv_sqr


[eigenvector, eigenvalue] = eig(K_equ)
v1 = eigenvector(:,1) 
v2 = eigenvector(:,2) 

u1 = M_inv_sqr*-v1
u1_max_norm = u1/max(u1)
u2 = M_inv_sqr*v2
u2_max_norm = u2/max(u2)

% solving symbolically
A=[2 -4;-1 -1]
[V,D]=eig(A)

A_sym=sym([2 -4;-1 -1])
[V_sym,D_sym]=eig(A_sym)







