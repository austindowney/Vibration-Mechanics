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


tt = np.linspace(0,10,1000)

k= 20         # N/m
m = 3         # kg
c = 2       # kg/s
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
xi = c/c_critical
omega_d = omega_n*np.sqrt(1-xi**2)

x_0=25/1000   # mm
v_0=-0/1000   # mm/s 

# calculate the underdamped response. 
A = np.sqrt((v_0+xi*omega_n*x_0)**2+(x_0*omega_d)**2)/omega_d
theta = np.arctan((omega_d*x_0)/(v_0+xi*omega_n*x_0))
xx_underdamped = A*np.exp(-xi*omega_n*tt)*np.sin(omega_d*tt+theta)

xx_peak = A*np.exp(-xi*omega_n*tt)

#xx_underdamped = xx_underdamped + 0.001*np.random.randn(len(xx_underdamped))


plt.figure(figsize=(6,3))
plt.plot(tt,xx_underdamped*1000,label='data')
plt.plot(tt,xx_peak*1000,'k--',label='envelope of maximum values')
plt.plot(tt,-xx_peak*1000,'k--')


plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.xlim(0,10)
plt.ylim(-28,28)
plt.tight_layout()
plt.legend(loc=1,ncol=3)
plt.savefig('Logarithmic_decrement',dpi=300)













































































