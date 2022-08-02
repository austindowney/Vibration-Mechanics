# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import modules
import IPython as IP
IP.get_ipython().magic('reset -sf')

import warnings     # added to ignore the plotting warings about font types in math mode
warnings.simplefilter("ignore", UserWarning)

import matplotlib as mpl
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import os as os
import numpy as np
import scipy as sp
import copy as copy
from matplotlib import cm
import time
#import pykrige as pykrige
import scipy.io as sio
tt1 = time.time()

plt.close('all')



#%% Problem 3



tt = np.linspace(0,10,1000)

k= 10         # N/m
m = 1         # kg
c = 15      # kg/s
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response #1. 
x_0=1/1000   # mm
v_0=0/1000   # mm/s 
a_1 = (-v_0+(-zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
a_2 = (v_0+(zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
xx_overdamped_1 = np.exp(-zeta*omega_n*tt)*(
        a_1*np.exp(-omega_n*np.sqrt(zeta**2-1)*tt)+
        a_2*np.exp( omega_n*np.sqrt(zeta**2-1)*tt))

# calculate the underdamped response #2. 
x_0=1/1000   # mm
v_0=2/1000   # mm/s 
a_1 = (-v_0+(-zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
a_2 = (v_0+(zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
xx_overdamped_2 = np.exp(-zeta*omega_n*tt)*(
        a_1*np.exp(-omega_n*np.sqrt(zeta**2-1)*tt)+
        a_2*np.exp( omega_n*np.sqrt(zeta**2-1)*tt))

# calculate the underdamped response #3. 
x_0=0/1000   # mm
v_0=1/1000   # mm/s 
a_1 = (-v_0+(-zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
a_2 = (v_0+(zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
xx_overdamped_3 = np.exp(-zeta*omega_n*tt)*(
        a_1*np.exp(-omega_n*np.sqrt(zeta**2-1)*tt)+
        a_2*np.exp( omega_n*np.sqrt(zeta**2-1)*tt))

# calculate the underdamped response #4. 
x_0=0/1000   # mm
v_0=2/1000   # mm/s 
a_1 = (-v_0+(-zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
a_2 = (v_0+(zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
xx_overdamped_4 = np.exp(-zeta*omega_n*tt)*(
        a_1*np.exp(-omega_n*np.sqrt(zeta**2-1)*tt)+
        a_2*np.exp( omega_n*np.sqrt(zeta**2-1)*tt))



plt.figure(figsize=(6,3))
plt.plot(tt,xx_overdamped_1*1000,'-',label='$x_0=1$ mm; $v_0=0$ mm/s')
plt.plot(tt,xx_overdamped_2*1000,'--',label='$x_0=1$ mm; $v_0=2$ mm/s')
plt.plot(tt,xx_overdamped_3*1000,'-.',label='$x_0=0$ mm; $v_0=1$ mm/s')
plt.plot(tt,xx_overdamped_4*1000,':',label='$x_0=0$ mm; $v_0=2$ mm/s')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
plt.legend(loc=1,ncol=2,framealpha=1)
plt.savefig('Over_damped_various_initial_conditions',dpi=300)





























































































