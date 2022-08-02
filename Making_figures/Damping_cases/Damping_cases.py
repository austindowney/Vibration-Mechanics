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
c = 2       # kg/s
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

x_0=1/1000   # mm
v_0=0/1000   # mm/s 

# calculate the underdamped response. 
A = np.sqrt((v_0+zeta*omega_n*x_0)**2+(x_0*omega_d)**2)/omega_d
theta = np.arctan((omega_d*x_0)/(v_0+zeta*omega_n*x_0))
xx_underdamped = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_d*tt+theta)

# calculate the overdamped response
c = 25
zeta = c/c_critical
a_1 = (-v_0+(-zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))
a_2 = (v_0+(zeta+np.sqrt(zeta**2-1))*omega_n*x_0)/(2*omega_n*np.sqrt(zeta**2-1))


xx_overdamped = np.exp(-zeta*omega_n*tt)*(
        a_1*np.exp(-omega_n*np.sqrt(zeta**2-1)*tt)+
        a_2*np.exp( omega_n*np.sqrt(zeta**2-1)*tt)
        )

## calculate the critically response
c = c_critical
zeta = c/c_critical
a_1 = x_0
a_2 = v_0+omega_n*x_0
xx_criticallydamped = (a_1+a_2*tt)*np.exp(-omega_n*tt)



#((-zeta+np.sqrt(zeta**2-1))*omega_n*x_0-v_0)
#
#
#(-x_0*omega_n*(zeta-np.sqrt(zeta**2-1))-v_0)




plt.figure(figsize=(6,3))
plt.plot(tt,xx_underdamped*1000,label='under damped case')
plt.plot(tt,xx_overdamped*1000,'--',label='over damped case')
plt.plot(tt,xx_criticallydamped*1000,':',label='critically damped case')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1)
plt.savefig('Damping_cases',dpi=300)





























































































