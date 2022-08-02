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


D = np.loadtxt('vibration_data.csv',delimiter=',')

A = np.loadtxt('time_data.csv',delimiter=',')

tt = A[:,0]
aa1 = A[:,1]
aa2 = A[:,2]

x = D[:,0]
y1 = D[:,1]
y2 = D[:,2]

plt.figure(figsize=(4.9,4))
plt.subplot(2,1,1)
plt.plot(tt,aa1,linewidth=0.6)
plt.xlim([0,200])
plt.grid('on')
plt.ylabel('acceleration (mg)')
plt.xlabel('time (s)')
plt.title('temporal response of the light pole')

plt.subplot(2,1,2)
plt.ylabel('power')
plt.xlabel('frequency (Hz)')
plt.semilogy(x,y1)
plt.grid('on')
plt.ylim([0.7,200000])
plt.yticks([1,100,10000,])
plt.xlim([0,23])
plt.title('temporal response of the light pole')
plt.tight_layout()
plt.savefig('Python.pdf')


#plt.legend(loc=1,ncol=2,framealpha=1)







# plt.figure(figsize=(6,3))
# # plt.subplot(2,1,1)
# plt.plot(tt,aa1,linewidth=0.6)
# plt.grid('on')
# plt.ylabel('amplitude (mm)')

# plt.tight_layout()
# plt.savefig('Python.pdf')


#plt.legend(loc=1,ncol=2,framealpha=1)
























































































