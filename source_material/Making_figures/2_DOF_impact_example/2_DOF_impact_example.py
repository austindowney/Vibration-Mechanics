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


#%% for a forced response for a underdamped system with the forcing function being cos. 





F_0 = 10
m_1 = 1000
m_2 = 1100
k = 1500
omega=np.sqrt(k*(1/m_1+1/m_2)) 

t = np.linspace(0,10,1000)

x_1 = F_0/(m_1+m_2)*(t+m_2/(omega*m_1)*np.sin(omega*t))
x_2 = F_0/(m_1+m_2)*(t-1/(omega)*np.sin(omega*t))


plt.figure(figsize=(6.5,3))
plt.plot(t,x_1,label='$x_1$')
plt.plot(t,x_2,'--',label='$x_2$')
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('displacement (m)')
plt.tight_layout()
plt.legend(framealpha=1)
plt.savefig('2_DOF_impact_example',dpi=300)
plt.savefig('2_DOF_impact_example.pdf',dpi=300)




























































