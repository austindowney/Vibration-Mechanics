#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Default plotting code for Open_Vibrations that sets the fonts and format.

@author: Austin Downey
"""

#%% import modules and set default fonts and colors

# import IPython as IP
# IP.get_ipython().magic('reset -sf')

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



r = np.linspace(0,2,300)

# solve for the table used in building the plot on the board
r_table = np.arange(0,2.25,0.25)
Xk_F_table = np.zeros((4,9))


zeta_1 = 0.1
Xk_F_1 = 1/(np.sqrt((1-r**2)**2+(2*zeta_1*r)**2))
Xk_F_table[0,:] = 1/(np.sqrt((1-r_table**2)**2+(2*zeta_1*r_table)**2))
phase_1 = np.arctan((2*zeta_1*r)/(1-r**2))
phase_1[150::] = phase_1[150::] + np.pi #adjust for atan aliasing at pi

zeta_2 = 0.25
Xk_F_2 = 1/(np.sqrt((1-r**2)**2+(2*zeta_2*r)**2))
Xk_F_table[0,:] = 1/(np.sqrt((1-r_table**2)**2+(2*zeta_2*r_table)**2))
phase_2 = np.arctan((2*zeta_2*r)/(1-r**2))
phase_2[150::] = phase_2[150::] + np.pi #adjust for atan aliasing at pi

zeta_3 = 0.5
Xk_F_3 = 1/(np.sqrt((1-r**2)**2+(2*zeta_3*r)**2))
Xk_F_table[0,:] = 1/(np.sqrt((1-r_table**2)**2+(2*zeta_3*r_table)**2))
phase_3 = np.arctan((2*zeta_3*r)/(1-r**2))
phase_3[150::] = phase_3[150::] + np.pi #adjust for atan aliasing at pi

zeta_4 = 0.707107
Xk_F_4 = 1/(np.sqrt((1-r**2)**2+(2*zeta_4*r)**2))
Xk_F_table[1,:] = 1/(np.sqrt((1-r_table**2)**2+(2*zeta_4*r_table)**2))
phase_4 = np.arctan((2*zeta_4*r)/(1-r**2))
phase_4[150::] = phase_4[150::] + np.pi #adjust for atan aliasing at pi

zeta_5 = 1
Xk_F_5 = 1/(np.sqrt((1-r**2)**2+(2*zeta_5*r)**2))
Xk_F_table[2,:] = 1/(np.sqrt((1-r_table**2)**2+(2*zeta_5*r_table)**2))
phase_5 = np.arctan((2*zeta_5*r)/(1-r**2))
phase_5[150::] = phase_5[150::] + np.pi #adjust for atan aliasing at pi

zeta_6 = 2
Xk_F_6 = 1/(np.sqrt((1-r**2)**2+(2*zeta_6*r)**2))
Xk_F_table[3,:] = 1/(np.sqrt((1-r_table**2)**2+(2*zeta_6*r_table)**2))
phase_6 = np.arctan((2*zeta_6*r)/(1-r**2))
phase_6[150::] = phase_6[150::] + np.pi #adjust for atan aliasing at pi


# round the values in the table
Xk_F_table = np.round(Xk_F_table,2)

# build a vector of r-peak values
zetas = np.linspace(0,1/np.sqrt(2))
r_peaks = np.sqrt(1-2*zetas**2)
peaks = 1/(np.sqrt((1-r_peaks**2)**2+(2*zetas*r_peaks)**2))

# plot the figures
plt.figure(figsize=(6.5,4.5))
plt.plot(r_peaks,peaks,'gray')
t = plt.text(0.4,4.5,'$r_\r{peak}$ locations',fontsize=13)
t.set_bbox(dict(facecolor='white', alpha=1, edgecolor='white'))
plt.plot(r,Xk_F_1,'-',lw=0.9,label='$\zeta=$'+str(zeta_1))
plt.plot(r,Xk_F_2,'--',label='$\zeta=$'+str(zeta_2))
plt.plot(r,Xk_F_3,':',label='$\zeta=$'+str(zeta_3))
plt.plot(r,Xk_F_4,'-.',label='$\zeta=1/\sqrt{2}$')
plt.plot(r,Xk_F_5,'-',lw=2.5,label='$\zeta=$'+str(zeta_5))
plt.plot(r,Xk_F_6,'--',lw=2.5,label='$\zeta=$'+str(zeta_6))
plt.ylim(-0.15,5.15)
plt.legend(framealpha=1)
plt.grid('on')
plt.xlabel(r'frequency ratio ($r$)')
plt.ylabel('normalized amplitude ($Xk/F_0$)')
plt.tight_layout()
#plt.savefig('underdamped_frequency_response_amplitude',dpi=300)
plt.savefig('underdamped_frequency_response_amplitude.pdf',dpi=300)


# plt.figure(figsize=(6.5,4.5))
# plt.plot(r,phase_1,'-',lw=0.9,label='$\zeta=$'+str(zeta_1))
# plt.plot(r,phase_2,'--',label='$\zeta=$'+str(zeta_2))
# plt.plot(r,phase_3,':',label='$\zeta=$'+str(zeta_3))
# plt.plot(r,phase_4,'-.',label='$\zeta=1/\sqrt{2}$')
# plt.plot(r,phase_5,'-',lw=2.5,label='$\zeta=$'+str(zeta_5))
# plt.plot(r,phase_6,'--',lw=2.5,label='$\zeta=$'+str(zeta_6))
# plt.hlines(np.pi/2,0,2,linestyle = '--')
# plt.legend(framealpha=1)
# plt.grid('on')
# plt.xlabel(r'frequency ratio ($r$)')
# plt.ylabel('phase (rad)')
# plt.tight_layout()
# plt.savefig('underdamped_frequency_response_phase',dpi=300)


plt.figure(figsize=(6.5,4.5))
plt.plot(r,phase_1*(180/np.pi),'-',lw=0.9,label='$\zeta=$'+str(zeta_1))
plt.plot(r,phase_2*(180/np.pi),'--',label='$\zeta=$'+str(zeta_2))
plt.plot(r,phase_3*(180/np.pi),':',label='$\zeta=$'+str(zeta_3))
plt.plot(r,phase_4*(180/np.pi),'-.',label='$\zeta=1/\sqrt{2}$')
plt.plot(r,phase_5*(180/np.pi),'-',lw=2.5,label='$\zeta=$'+str(zeta_5))
plt.plot(r,phase_6*(180/np.pi),'--',lw=2.5,label='$\zeta=$'+str(zeta_6))
plt.hlines(np.pi/2*(180/np.pi),1,2,color = 'black', linestyle = '--',lw=2)
plt.yticks((0,45,90,135,180))
plt.ylim([-10,190])
plt.legend(framealpha=1)
t = plt.text(1.05,79,'shifted up by $\pi$ for plotting',fontsize=13)
t.set_bbox(dict(facecolor='white', alpha=1, edgecolor='white'))
plt.grid('on')
plt.xlabel(r'frequency ratio ($r$)')
plt.ylabel('phase (deg)')
plt.tight_layout()
plt.savefig('underdamped_frequency_response_phase',dpi=300)











