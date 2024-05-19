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


#%% plot the resonant response

tt = np.linspace(0,10,1000)

x_0=1/1000   # mm
v_0=0/1000   # mm/s 
k= 50         # N/m
m = 1         # kg
c = 0.9       # kg/s
omega_n = np.sqrt(k/m) # rad/sec
omega=omega_n
f_0=1
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

xx = (v_0/omega)* np.sin(omega*tt) + x_0 * np.cos(omega*tt) + f_0/(2*omega)*tt*np.sin(omega*tt)

xx_outline = f_0/(2*omega)*tt

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.plot(tt,xx_outline*1000,'k--',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.plot(tt,-xx_outline*1000,'k--',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
#plt.legend(loc=1,ncol=2,framealpha=1)
plt.savefig('Python.pdf')





























































































