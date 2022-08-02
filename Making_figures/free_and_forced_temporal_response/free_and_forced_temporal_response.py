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



#%% free_and_forced_temporal_response

cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
tt = np.linspace(0,7,1000)

k= 10           # N/m
m = 2.5         # kg
omega_n = np.sqrt(10/2.5) # rad/sec
omega = 4 # rad/sec
F_0 = 0.1 # kN
f_0 = F_0/m 

x_0 = 1/1000         # mm
v_0 = 0/1000     # mm/s 
xx_1 = v_0/omega_n*np.sin(omega_n*tt) + x_0*np.cos(omega_n*tt)

xx_2 = v_0/omega_n*np.sin(omega_n*tt) + (x_0-f_0/(omega_n**2-omega**2))*np.cos(omega_n*tt) + (f_0/(omega_n**2-omega**2))*np.cos(omega*tt)
xx_forcing = F_0*np.cos(omega*tt)

fig, ax1 = plt.subplots(figsize=(5.5,3))
t = np.arange(0.01, 10.0, 0.01)
lns1 = ax1.plot(tt,xx_1*1000,color=cc[0],label='free vibration')
lns2 = ax1.plot(tt,xx_2*1000,'--',color=cc[1],label='forced vibration')
ax1.set_xlabel('time (s)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('displacement amplitude (mm)')
#ax1.tick_params('y', co)


ax2 = ax1.twinx()
s2 = np.sin(2 * np.pi * t)
lns3 = ax2.plot(tt,xx_forcing*1000,':',color=cc[2],label='forcing function',zorder=0)
ax2.set_ylabel('applied force (N)', color=cc[2])
ax2.tick_params('y', colors=cc[2])


# added these three lines
lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=3, framealpha=1)

fig.tight_layout()
plt.show()

plt.savefig('free_and_forced_temporal_response.png',dpi=300)

































































