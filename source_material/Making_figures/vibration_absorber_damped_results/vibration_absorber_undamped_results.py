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


omega_2 = omega_1# set the two frequencies the same
#omega_2 = np.sqrt(k_2/m_2)

k_2 = omega_2**2*m_2




beta = omega_2/omega_1
mu = m_2/m_1
r = omega/omega_1

def damped_abs(c):
    
    zeta = c/(2* m_2 * omega_1)
    numerator = (2 * zeta * r)**2 + (r**2 - beta**2)**2
    denominator_1 = (2 * zeta * r)**r * (r**2 -1 + mu * r**2)**2
    denominator_2  = ( mu*r**2*beta**2 - (r**2 - 1)*(r**2 - beta**2))**2
    denominator = denominator_1 + denominator_2
    mass_damped_absorber = np.sqrt(numerator/denominator)
    
    return(mass_damped_absorber,zeta)

c = 0.6
mass_damped_absorber_1,zeta_1 = damped_abs(c)
c = 0.2
mass_damped_absorber_2,zeta_2 = damped_abs(c)
c = 0.06
mass_damped_absorber_3,zeta_3 = damped_abs(c)
c = 0.004
mass_damped_absorber_4,zeta_4 = damped_abs(c)



# solve for the system with an undamped vibration absorber
mass_undamped_absorber = (1-r**2)/ ((1 + k_2/k_1 - r**2) * (1-r**2) - k_2/k_1)
mass_undamped_absorber = np.abs(mass_undamped_absorber)

# solve for the system without a vibration absorber
mass_without_absorber = 1/(1-r**2)
mass_without_absorber = np.abs(mass_without_absorber)


plt.figure(figsize=(6.5,2.8))
plt.plot(r,mass_damped_absorber_1,'-',label='damped absorber\nwith $\zeta=$'+str(np.round(zeta_1,3)))
plt.plot(r,mass_damped_absorber_2,'--',label='damped absorber\nwith $\zeta=$'+str(np.round(zeta_2,4)))
plt.plot(r,mass_damped_absorber_3,'-.',label='damped absorber\nwith $\zeta=$'+str(np.round(zeta_3,4)))
plt.plot(r,mass_damped_absorber_4,':',label='damped absorber\nwith $\zeta=$'+str(np.round(zeta_4,4)))
# plt.plot(r,mass_undamped_absorber,color='gray',label='undamped absorber')
# plt.plot(r,mass_without_absorber,'--',color='gray',label='without absorber')
plt.ylim([0,17])
plt.xlim([0.5,1.5])
plt.legend(framealpha=1)
plt.grid(True)
plt.xlabel(r'$\omega $ / $ \omega_1$')
plt.ylabel(r'$X_1 $ / $\delta_\textnormal{st}$')
plt.tight_layout()
plt.savefig('vibration_absorber_damped_results',dpi=300)























