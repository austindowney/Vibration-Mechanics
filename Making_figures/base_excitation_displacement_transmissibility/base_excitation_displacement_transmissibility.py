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


r = np.linspace(0,3,300)

# solve for the table used in building the plot on the board
r_table = np.arange(0,2.25,0.25)
Xk_F_table = np.zeros((4,9))


zeta_1 = 0.1
Xk_F_1 = np.sqrt((1+(2*zeta_1*r)**2)/((1-r**2)**2+(2*zeta_1*r)**2)) 


zeta_2 = 0.25
Xk_F_2 = np.sqrt((1+(2*zeta_2*r)**2)/((1-r**2)**2+(2*zeta_2*r)**2)) 

zeta_3 = 0.5
Xk_F_3 = np.sqrt((1+(2*zeta_3*r)**2)/((1-r**2)**2+(2*zeta_3*r)**2)) 

zeta_4 = 0.707107
Xk_F_4 = np.sqrt((1+(2*zeta_4*r)**2)/((1-r**2)**2+(2*zeta_4*r)**2)) 

zeta_5 = 1
Xk_F_5 = np.sqrt((1+(2*zeta_5*r)**2)/((1-r**2)**2+(2*zeta_5*r)**2)) 

zeta_6 = 2
Xk_F_6 = np.sqrt((1+(2*zeta_6*r)**2)/((1-r**2)**2+(2*zeta_6*r)**2)) 


# round the values in the table
Xk_F_table = np.round(Xk_F_table,2)

# plot the figures
plt.figure(figsize=(6.5,4))
plt.plot(r,Xk_F_1,'-',lw=0.9,label='$\zeta=$'+str(zeta_1))
plt.plot(r,Xk_F_2,'--',label='$\zeta=$'+str(zeta_2))
plt.plot(r,Xk_F_3,':',label='$\zeta=$'+str(zeta_3))
plt.plot(r,Xk_F_4,'-.',label='$\zeta=1/\sqrt{2}$')
plt.plot(r,Xk_F_5,'-',lw=2.5,label='$\zeta=$'+str(zeta_5))
plt.plot(r,Xk_F_6,'--',lw=2.5,label='$\zeta=$'+str(zeta_6))
plt.vlines(np.sqrt(2),-1,10,linestyle='--')
plt.legend(framealpha=1)
plt.grid('on')
plt.ylim([-0.5,5.5])
plt.xlim([0,2.5])
plt.xlabel(r'frequency ratio ($\beta$)')
plt.ylabel(r'displacement ratio ($X/Y$)')
plt.tight_layout()
plt.savefig('python.pdf')



















