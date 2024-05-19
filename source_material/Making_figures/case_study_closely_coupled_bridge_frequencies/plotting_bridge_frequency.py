#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import IPython as IP
IP.get_ipython().magic('reset -sf')

#%% import modules and set default fonts and colors

"""
Default plot formatting code for Austin Downey's series of open source notes/
books. This common header is used to set the fonts and format.

Header file last updated March 10, 2024
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl


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
## End of plot formatting code

plt.close('all')


#%% Load the modules needed for this code. 

import pandas as PD
from scipy import interpolate
import pickle
import time
import re
import json as json
import pylab
from scipy.fft import fft, fftfreq

#%% Problem 3

data = np.loadtxt('Data.csv',delimiter=',',skiprows=1,usecols=[0,1])

tt = data[:40000,1]
aa = data[:40000,0]


plt.figure(figsize=(6,3))
plt.ylabel('acceleration (m/s$^2$)')
plt.xlabel('time (m)')
plt.plot(tt/60,aa)
plt.grid()
plt.tight_layout()




# Number of sample points
N = aa.shape[0]
# sample spacing
T = tt[1]-tt[0]
yf = fft(aa)
xf = fftfreq(N, T)[:N//2]
y = 2.0/N * np.abs(yf[0:N//2])

plt.figure(figsize=(6,3))
plt.plot(xf, y,lw=0.4)
plt.ylabel('power')
plt.xlabel('frequency (Hz)')
plt.xlim([0,20])
plt.ylim([0,0.0062])
center_1 = 3.97
offset_1 = 0.9
plt.text(center_1,0.0032,'first modes of\nindividual bridge\ncomponents ',ha='center',bbox=dict(facecolor='white',edgecolor='none', alpha=1))
plt.vlines(center_1+offset_1,0,0.1,colors=cc[1],linestyle='--')
plt.vlines(center_1-offset_1,0,0.1,colors=cc[1],linestyle='--')

center_2 = 12.79
offset_2 = 1.5
plt.text(center_2,0.0047,'second modes of\nindividual bridge\ncomponents ',ha='center',bbox=dict(facecolor='white',edgecolor='none', alpha=1))
plt.vlines(center_2+offset_2,0,0.1,colors=cc[1],linestyle='--')
plt.vlines(center_2-offset_2,0,0.1,colors=cc[1],linestyle='--')
plt.grid()
plt.tight_layout()

plt.savefig('case_study_closely_coupled_bridge_frequencies_2.jpg',dpi=300)


# plt.figure(figsize=(6,3))
# plt.plot(tt,xx_underdamped*1000,label='under damped case')
# plt.plot(tt,xx_overdamped*1000,'--',label='over damped case')
# plt.plot(tt,xx_criticallydamped*1000,':',label='critically damped case')
# plt.grid('on')
# plt.ylabel('amplitude (mm)')
# plt.xlabel('time (s)')
# plt.tight_layout()
# plt.legend(loc=1,ncol=3,framealpha=1)
# plt.savefig('Damping_cases',dpi=300)





























































































