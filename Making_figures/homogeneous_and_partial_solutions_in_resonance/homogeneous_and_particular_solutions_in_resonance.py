#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:30:27 2016

@author: downey
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
plt.rcParams.update({'image.cmap': 'viridis'})
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
 'Century Schoolbook L',  'Utopia', 'ITC Bookman', 'Bookman', 
 'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.fontset': 'custom'})
plt.close('all')

#%% Load the expermintal data


# define the time steps
tt = np.linspace(0,10,1000)


#%% Plot configuration a

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 1      # N
omega = 8.162  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-10,10)
plt.xlim([0,8])
#plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega$='+str(omega),size=15)
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[1,1.2,0,0])
plt.tight_layout()
plt.savefig('homogeneous_and_partial_solutions_in_resonance_a.png',dpi=300)




#%% for varying initial conditions

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 3      # N
omega = 8.162  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-10,10)
plt.xlim([0,8])
#plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega$='+str(omega),size=15)
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[1,1.2,0,0])
plt.tight_layout()
plt.savefig('homogeneous_and_partial_solutions_in_resonance_b.png',dpi=300)



#%% for varying initial conditions

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 3      # N
#omega = 5  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
omega = omega_n
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-100,100)
plt.xlim([0,8])
#plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega$='+str(omega),size=15)
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[1,1.2,0,0])
plt.tight_layout()
plt.savefig('homogeneous_and_partial_solutions_in_resonance_c.png',dpi=300)





















