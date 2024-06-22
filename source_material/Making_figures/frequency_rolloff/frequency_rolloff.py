#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import IPython as IP
IP.get_ipython().run_line_magic('reset', '-sf')

#%% import modules and set default fonts and colors

"""
Default plot formatting code for Austin Downey's series of open source notes/
books. This common header is used to set the fonts and format.

Header file last updated May 16, 2024
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl


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
# I don't think I need this next line as its set to 'stixsans' above. 
plt.rcParams.update({'mathtext.fontset': 'custom'}) 
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
## End of plot formatting code

plt.close('all')


import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

#%% free_and_forced_temporal_response

plt.figure(figsize=(6.5,2.5))

plt.semilogx()
plt.grid(True)
plt.yticks([-60,-50,-40,-30,-20,-10,0,10])
xticks = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
xlabels = ['0.001', '0.01', '0.1', '1', '10', '100', '1000']
plt.xticks(xticks, xlabels)

plt.xlabel('angular frequency (rad/sec)')
plt.ylabel('gain (dB)')
plt.tight_layout()
plt.savefig('python.pdf')

































































