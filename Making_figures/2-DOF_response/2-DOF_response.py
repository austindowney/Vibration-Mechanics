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


#%% 

tt = np.linspace(0,20,1000)

xx_1 = 1/2*(np.cos(np.sqrt(2)*tt) + np.cos(2*tt))
xx_2 = 3/2*(np.cos(np.sqrt(2)*tt) - np.cos(2*tt))


plt.figure(figsize=(6,3))
plt.plot(tt,xx_1,label='$x_1$')
plt.plot(tt,xx_2,'--',label='$x_2$')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.xlim([0,20])
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('2-DOF_response.png',dpi=300)
























