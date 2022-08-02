# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% import modules
import IPython as IP
IP.get_ipython().magic('reset -sf')
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import os as os
import numpy as np
import scipy as sp
from scipy.interpolate import griddata
from matplotlib import cm
import time
import subprocess
import pickle
import scipy.io as sio
import sympy as sym
from matplotlib import cm
import re as re
from scipy import signal
from scipy import fft
import json as json
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d as mp3d


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



#%% build the data


tt = np.linspace(0,10,num=100000)
T = tt[1]-tt[0]
fs = 1/T
x = sp.signal.chirp(tt,0,tt[-1],10,method='linear')
f, t, Sxx = signal.spectrogram(x, fs, nperseg=10000,noverlap=4000)
#f, t, Sxx = sp.signal.spectrogram(x, fs,window=('tukey', 50), nperseg=100, noverlap=None,)





#%% Plot the spectrogram 

plt.figure(figsize=(6.5,3.5))

plt.subplot(2,1,1)
plt.plot(tt,x,lw=0.6)
plt.xlim([0,10])
plt.grid(True)
plt.ylabel('$x(t)$')

plt.subplot(2,1,2)
#plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.imshow(Sxx, aspect='auto', origin='lower',extent=(0,10,0,5000))
plt.ylabel('frequency (Hz)')
plt.xlabel('time (s)')
plt.ylim([0,12])
plt.xlim([0,10])
plt.tight_layout()
plt.savefig('spectrogram',dpi=500)





# plt.figure(figsize=(5, 4))
# plt.imshow(Sxx, aspect='auto', origin='lower')
# plt.title('Spectrogram')
# plt.ylabel('Frequency band')
# plt.xlabel('Time window')
# plt.ylim([0,12])
# plt.tight_layout()






















