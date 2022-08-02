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


#%% Load the expermintal data

tt = np.linspace(0,12,1000)

k= 500         # N/m
m = 10         # kg
c = 0       # kg/s
omega = 8.162
F_0 = 100
f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)


x_0=0.00   # m
v_0=0.00   # m/s 

# calculate the underdamped response. 
X = f_0/(omega_n**2-omega**2)
A = np.sqrt((v_0/omega_n)**2+(x_0-X)**2)
theta = np.arctan((omega_n*(x_0-X))/(v_0))
xx_h = A*np.sin(omega_n*tt+-0)
xx_p = X*np.cos(omega*tt)
xx_underdamped = xx_h + xx_p


plt.figure(figsize=(6,3))
plt.plot(tt,xx_h*1000,':',lw=1.5,label='homogeneous solution')
plt.plot(tt,xx_p*1000,'--',lw=1.5,label='particular solution')
plt.plot(tt,xx_underdamped*1000,'-',lw=1,label='total solution')
plt.xlim(0,12)
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('homogeneous_and_particular_solutions.png',dpi=300)




omega_n/(v_0)


#7.0710678118654755/(0.0)



