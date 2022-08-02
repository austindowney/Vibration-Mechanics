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



#%% plot the resonant response

stiffness = 16350.
kg = np.array([5,10,15,20,25,30])
force = kg*9.81
displacement = force/stiffness # np.array([0.001,0.004,0.007,0.01,0.013,0.016])

omega_n = np.sqrt(stiffness/kg)

plt.figure(figsize=(6,3))
plt.plot(displacement,force,'o--')
plt.xlabel('displacement (m)')
plt.ylabel('force (N)')
plt.grid(True)
plt.tight_layout()
plt.savefig('Linear_spring_deformation_plot_with_frequency_force',dpi=300)

plt.figure(figsize=(6,3))
plt.plot(kg,omega_n,'o--')
plt.xlabel('mass (kg)')
plt.ylabel('$\omega_n$')
plt.grid(True)
plt.tight_layout()
plt.savefig('Linear_spring_deformation_plot_with_frequency_frequency',dpi=300)


























































































