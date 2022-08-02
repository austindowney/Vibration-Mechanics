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

F_0 = 1
k = 10
c = 1
m = 1
c_cr = 2*np.sqrt(k*m)
zeta = c/c_cr
omega_n = np.sqrt(k/m)
omega_d = omega_n*np.sqrt(1-zeta**2)
theta = np.arctan(zeta/np.sqrt(1-zeta**2))#-np.pi/2

tt = np.linspace(0,10,1000)

xx_undamped_impulse = 1/(m*omega_d)*np.exp(0*omega_n*tt)*np.sin(omega_d*tt)#F_0/k*(1-np.cos(omega_n*tt))
xx_underdamped_impulse = 1/(m*omega_d)*np.exp(-zeta*omega_n*tt)*np.sin(omega_d*tt)


plt.figure(figsize=(6,3))
plt.plot(tt,xx_undamped_impulse*1000,label='undamped')
plt.plot(tt,xx_underdamped_impulse*1000,'--',label='underdamped')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('response_impulse.png',dpi=300)








