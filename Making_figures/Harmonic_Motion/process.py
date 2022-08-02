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
import json as json
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d as mp3d

plt.close('all')
cc = plt.rcParams['axes.prop_cycle'].by_key()['color'] 

#%% Plot the figure



omega = 5
phi = 0
A=1

tt = np.linspace(0,3.845,1000)
xx = A*np.sin(omega*tt+phi)
xx2 = A*np.sin(2*omega*tt+phi)
xx3 = A*np.sin(3*omega*tt+phi)
xx4 = A*np.sin(4*omega*tt+phi)

plt.figure()
plt.plot(tt,xx)
plt.savefig('python.pdf')




plt.figure()
plt.plot(tt,xx+xx2+xx3+xx4)
plt.savefig('python.pdf')























