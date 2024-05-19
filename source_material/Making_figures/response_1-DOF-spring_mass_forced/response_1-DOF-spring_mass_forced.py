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




tt = np.linspace(0,10,1000)

x_1 = (10/np.sqrt(20)*0.1/(20-10**2))*np.sin(np.sqrt(20)*tt) + 0 + 0.1/(20-10**2)*np.sin(10*tt)
x_2 = (10/np.sqrt(20)*0.1/(20-10**2))*np.sin(np.sqrt(20)*tt) + 0.005*np.cos(np.sqrt(20)*tt) + 0.1/(20-10**2)*np.sin(10*tt)


plt.figure(figsize=(6.5,3))
plt.plot(tt,x_1*1000,label='$x_0=0$, $v_0=0$')
plt.plot(tt,x_2*1000,'--',label='$x_0=0.005$, $v_0=0$')
plt.xlim([0,10])
plt.xlabel('time (s)')
plt.ylabel('displacement (mm)')
plt.grid('on')
plt.legend(loc=1,ncol=2,framealpha=1)
plt.tight_layout()

plt.savefig('response_1-DOF-spring_mass_forced.png',dpi=300)








