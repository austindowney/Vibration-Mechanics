#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import IPython as IP
IP.get_ipython().magic('reset -sf')

#%% import modules and set default fonts and colors

"""
Default plot formatting code for Austin Downey's series of open source notes/
books. This common header is used to set the fonts and format.

Last updated March 10, 2024
"""
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
## End of plot formatting code

plt.close('all')

#%% plot the arctan


tt = np.linspace(-62,62,1000)

plt.figure(figsize=(6,3))
plt.plot(tt,np.arctan(tt))



plt.grid('on')
plt.ylabel('$y(x)$')
plt.gca().set_yticklabels(['$-\pi/2$','${-\pi}/{4}$',0,'${\pi}/{4}$','${\pi}/{2}$'])
plt.yticks([-np.pi/2,-np.pi/4,0,np.pi/4,np.pi/2])
plt.xlim([-61,61])
plt.xlabel('$x$')
plt.tight_layout()
plt.savefig('arctan_plot',dpi=250)













































































