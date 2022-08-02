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

#%% for a forced response for a underdamped system with the forcing function being cos. 


r = np.linspace(0,2,300)

# solve for the table used in building the plot on the board
r_table = np.arange(0,2.25,0.25)
Xk_F_table = np.zeros((4,9))


zeta_1 = 0.1
F_1 = r**2*np.sqrt((1+(2*zeta_1*r)**2)/((1-r**2)**2+(2*zeta_1*r)**2)) 
D_1 = np.sqrt((1+(2*zeta_1*r)**2)/((1-r**2)**2+(2*zeta_1*r)**2)) 


# round the values in the table
Xk_F_table = np.round(Xk_F_table,2)

# plot the figures
plt.figure(figsize=(6,3))
plt.plot(r,F_1,'-',lw=0.9,label='force transmissibility')
plt.plot(r,D_1,'--',label='displacement transmissibility')
plt.legend(framealpha=1)
plt.grid('on')
plt.xlabel('frequency ration ($r$)')
plt.ylabel('transmissibility (force or displacement)')
#plt.title('$\zeta$=0.1')
plt.tight_layout()
plt.savefig('base_excitation_force_and_displacement_transmissibility_1',dpi=300)




zeta_1 = 2
F_1 = r**2*np.sqrt((1+(2*zeta_1*r)**2)/((1-r**2)**2+(2*zeta_1*r)**2)) 
D_1 = np.sqrt((1+(2*zeta_1*r)**2)/((1-r**2)**2+(2*zeta_1*r)**2)) 


# round the values in the table
Xk_F_table = np.round(Xk_F_table,2)

# plot the figures
plt.figure(figsize=(6,3))
plt.plot(r,F_1,'-',lw=0.9,label='force transmissibility')
plt.plot(r,D_1,'--',label='displacement transmissibility')
plt.legend(framealpha=1)
plt.grid('on')
plt.xlabel('frequency ration ($r$)')
plt.ylabel('transmissibility (force or displacement)')
#plt.title('$\zeta$=2')
plt.tight_layout()
plt.savefig('base_excitation_force_and_displacement_transmissibility_2',dpi=300)






















