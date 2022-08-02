#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Default plotting code for Open_Vibrations that sets the fonts and format.

@author: Austin Downey
"""

#%% import modules and set default fonts and colors

import IPython as IP
IP.get_ipython().magic('reset -sf')

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as PD
import scipy as sp
from scipy import interpolate
import pickle
import time
import re
import json as json
import pylab

# set default fonts and plot colors
plt.rcParams.update({'text.usetex': True})
plt.rcParams.update({'image.cmap': 'viridis'})
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
 'Century Schoolbook L',  'Utopia', 'ITC Bookman', 'Bookman', 
 'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.fontset': 'custom'}) # I don't think I need this as its set to 'stixsans' above.
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.close('all')


#%% Solve for the displacement

m_1 = 1    # kg
m_2 = 3     # kg
m_3 = 1     # kg
# k_1 = 30    # N/m
# k_2 = 5    # N/m
x_1_0 = 1 # m
x_2_0 = 0 # mm
v_1_0 = 0 # mm
v_2_0 = 0 # mm

tt = np.linspace(0,20,1000)

M = np.zeros((3,3))
M[0,0]= m_1
M[1,1]= m_2
M[2,2]= m_3

# K = np.zeros((3,3))
# K[0,0]= k_1+k_2
# K[0,1]= -k_2
# K[1,0]= -k_2
# K[1,1]= k_2+k_3
K = np.array([[3,-3,0],[-3,6,-3],[0,-3,3]])

#F = np.zeros((2,1))

#x_0 = np.zeros(2)
#x_0[0] = x_1_0
#v_0 = np.zeros(2)

# solve the generlized eignevalue problem
[eig_value, eig_vect]=sp.linalg.eig(K,M)


omega_1 = np.round(np.real(np.sqrt(eig_value[0])),5)
omega_2 = np.round(np.real(np.sqrt(eig_value[1])),5)
omega_3 = np.round(np.real(np.sqrt(eig_value[2])),5)


v_1 =  eig_vect[:,0]
v_2 =  eig_vect[:,1]
v_3 =  eig_vect[:,2]

# convert the the standard form
#M_inv_sqrt = np.linalg.inv(np.sqrt(M))
#K_mass_norm = M_inv_sqrt@K@M_inv_sqrt

#[eig_value, eig_vect]=sp.linalg.eig(K_mass_norm)
# v_1 =  np.round(eig_vect[:,0]/eig_vect[0,0])
# v_2 =  np.round(eig_vect[:,1]/eig_vect[0,0])

# omega_1 = np.round(np.real(np.sqrt(eig_value[0])),5)
# omega_2 = np.round(np.real(np.sqrt(eig_value[1])),5)
# omega_3 = np.round(np.real(np.sqrt(eig_value[2])),5)


# v_1 =  eig_vect[:,0]
# v_2 =  eig_vect[:,1]
# v_3 =  eig_vect[:,2]

# u_1 = M_inv_sqrt@v_1
# u_2 = M_inv_sqrt@v_2
# u_3 = M_inv_sqrt@v_3

# u_1_norm = u_1/np.linalg.norm(u_1)
# u_2_norm = u_2/np.linalg.norm(u_2)
# u_3_norm = u_3/np.linalg.norm(u_3)

#alpha_1 = np.sqrt(1/(v_1.T@M@v_1))
#alpha_2 = np.sqrt(1/(v_2.T@M@v_2))
#alpha_3 = np.sqrt(1/(v_3.T@M@v_3))

u_1 = v_1#*alpha_1
u_2 = v_2#*alpha_2
u_3 = v_3#*alpha_3


u_1_norm = u_1/np.linalg.norm(u_1)
u_2_norm = u_2/np.linalg.norm(u_2)
u_3_norm = u_3/np.linalg.norm(u_3)


plt.figure(figsize=(6,3))
plt.plot(u_1_norm,'o-',label='mode 1 at '+str(np.round(omega_1,3))+' rad/sec')
plt.plot(u_2_norm,'s--',label='mode 2 at '+str(np.round(omega_2,3))+' rad/sec')
plt.plot(u_3_norm,'d:',label='mode 3 at '+str(np.round(omega_3,3))+' rad/sec')
plt.hlines(0,-2,3,'k')
plt.xlim(-0.1,2.1)
plt.grid(True)
plt.legend(framealpha=1)
plt.xlabel('mass number')
plt.ylabel('unit vector normalized displacement')
plt.tight_layout()



#%% Normalize the plot over 1.

u_1_norm = u_1/np.max(u_1)
u_2_norm = u_2/np.max(u_2)
u_3_norm = u_3/np.max(u_3)

plt.figure(figsize=(6,3))
plt.plot(u_1_norm,'o-',label='mode 1 at '+str(np.round(omega_1,3))+' rad/sec')
plt.plot(u_2_norm,'s--',label='mode 2 at '+str(np.round(omega_2,3))+' rad/sec')
plt.plot(u_3_norm,'d:',label='mode 3 at '+str(np.round(omega_3,3))+' rad/sec')
plt.hlines(0,-2,3,'k')
plt.xlim(-0.1,2.1)
plt.grid(True)
plt.legend(framealpha=1)
plt.xlabel('mass number')
plt.ylabel('normalized displacement')
plt.tight_layout()
plt.savefig('mode_shape_aiplane_example_generalized_eigenvalue',dpi=500)




# alpha_1 = np.sqrt(1/(v_1@M@v_1))
# alpha_2 = np.sqrt(1/(v_2@M@v_2))

# #build the modal matirx 
# P=np.vstack(([alpha_1*v_1],[alpha_2*v_2])).T

# #Check that the modes are normalized
# print(P.T@M@P)


# q_0 = P.T@M@x_0
# q_dot_0 = P.T@M@v_0

# q_t_1 = q_0[0]*np.cos(omega_1*tt) + (q_dot_0[0]/omega_1)*np.sin(omega_1*tt)
# q_t_2 = q_0[1]*np.cos(omega_2*tt) + (q_dot_0[1]/omega_2)*np.sin(omega_2*tt)

# x_1 = P[0,0]*q_t_1 + P[0,1]*q_t_2 
# x_2 = P[1,0]*q_t_1 + P[1,1]*q_t_2 



# x_1_truncated = P[0,0]*q_t_1
# x_2_truncated = P[1,0]*q_t_1

# #%% Plots

# # Plot the full response
# plt.figure(figsize=(6.5,3))
# plt.plot(tt,x_1,label='$x_1$')
# plt.plot(tt,x_2,'--',label='$x_2$')
# plt.xlabel('time (s)')
# plt.ylabel('displacement (mm)')
# plt.legend(framealpha=1,loc=1)
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('modal_analysis_free_vibration.png',dpi=500)

# # plot the truncated response
# plt.figure(figsize=(6.5,3))
# plt.plot(tt,x_1_truncated,label='$x_1$')
# plt.plot(tt,x_2_truncated,'--',label='$x_2$')
# plt.xlabel('time (s)')
# plt.ylabel('displacement (mm)')
# plt.legend(framealpha=1,loc=1)
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('modal_analysis_free_vibration_truncated.png',dpi=500)

# # plot the participation factors as a function of time. 
# plt.figure(figsize=(6.5,3))
# plt.plot(tt,q_t_1,label='$q_1$')
# plt.plot(tt,q_t_2,'--',label='$q_2$')
# plt.xlabel('time (s)')
# plt.ylabel('participation')
# plt.legend(framealpha=1,loc=1)
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('modal_analysis_free_participation_factors.png',dpi=500)






