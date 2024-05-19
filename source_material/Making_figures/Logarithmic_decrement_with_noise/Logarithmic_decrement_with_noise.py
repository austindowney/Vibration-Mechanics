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




#%% Problem 3


tt = np.linspace(0,11,1000)

k= 43         # N/m
m = 3         # kg
c = 2.0       # kg/s
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

x_0=9/1000   # mm
v_0=35/1000   # mm/s 

# calculate the underdamped response. 
A = np.sqrt((v_0+zeta*omega_n*x_0)**2+(x_0*omega_d)**2)/omega_d
theta = np.arctan((omega_d*x_0)/(v_0+zeta*omega_n*x_0))
xx_underdamped = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_d*tt+theta)

xx_underdamped = xx_underdamped + 0.0005*np.random.randn(len(xx_underdamped))


plt.figure(figsize=(6,3.0))
plt.plot(tt,xx_underdamped*1000,lw=0.5,label='data')

plt.grid('on')
plt.ylabel('amplitude (mm)',labelpad=0)
plt.xlabel('time (s)')
plt.yticks([-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14])
plt.xticks(list(np.linspace(0,10,21)))
plt.xlim(0,10)
plt.tight_layout()
#plt.legend(loc=1,ncol=3)
plt.savefig('Logarithmic_decrement_with_noise_python',dpi=300)













































































