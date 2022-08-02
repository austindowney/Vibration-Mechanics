# -*- coding: utf-8 -*-
"""
Code for plotting plot

Austin Downey
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

#%% Plot the figure


# omega is the frequency of the entire system, and the one we will sweep over.
omega = np.linspace(0,2,1000)       # the frequencies we will sweep over

# setting a constant m_1 and m_2
m_1 = 20
m_2 = 1
F_0 = 1
k_1 = 20


delta_st = F_0/k_1

omega_1 = np.sqrt(k_1/m_1)
omega_2 = omega_1 #np.sqrt(k_2/m_2)

k_2 = omega_2**2*m_2

numerator = (1-(omega/omega_2)**2)

absorber_with = (1-(omega/omega_2)**2)/ ((1 + k_2/k_1 - (omega/omega_1)**2) * (1-(omega/omega_2)**2) - k_2/k_1)
absorber_with = np.abs(absorber_with)

absorber_without = 1/(1-(omega/omega_1)**2)
absorber_without = np.abs(absorber_without)


plt.figure(figsize=(6.5,3))
plt.plot(omega/omega_1,absorber_with,label='with absorber')
plt.plot(omega/omega_1,absorber_without,'--',label='without absorber')
plt.ylim([0,20])
plt.xlim([0.5,1.5])
plt.legend(framealpha=1)
plt.grid(True)
plt.xlabel(r'$\omega $ / $ \omega_1$')
plt.ylabel(r'$X_1 $ / $\delta_\textnormal{st}$')
plt.tight_layout()
plt.savefig('vibration_absorber_undamped_results',dpi=500)























