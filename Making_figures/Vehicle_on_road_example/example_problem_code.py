# -*- coding: utf-8 -*-
"""
base excitaiton car problem

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

#%% base excitaiton car problem. 

k = 300000 # N/m
m = 1600 # kg
v_kh = 50 # k/h
Y = 0.005   # m
c=15000 # kg/s
roughness_period = 3

# convert v from km/h to m/s

v_ms = v_kh*1000/3600 
omega_b = v_ms * (1/roughness_period ) * 2*np.pi


omega_n = np.sqrt(k/m)


beta = omega_b/omega_n

zeta = c / (2*np.sqrt(k*m))

a = 1+(2*zeta*beta)**2
b = (1-beta**2)**2+(2*zeta*beta)**2
X = Y*np.sqrt(a/b)
              
              
print(X)

























