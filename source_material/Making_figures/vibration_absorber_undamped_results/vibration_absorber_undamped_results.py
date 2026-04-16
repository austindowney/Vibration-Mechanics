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
omega_2 = omega_1 #np.sqrt(k_2/m_2)

k_2 = omega_2**2*m_2

numerator = (1-(omega/omega_2)**2)

absorber_with = (1-(omega/omega_2)**2)/ ((1 + k_2/k_1 - (omega/omega_1)**2) * (1-(omega/omega_2)**2) - k_2/k_1)
absorber_with = np.abs(absorber_with)

absorber_without = 1/(1-(omega/omega_1)**2)
absorber_without = np.abs(absorber_without)


plt.figure(figsize=(6.5,2.5))
plt.plot(omega/omega_1,absorber_with,label='with vibration absorber')
plt.plot(omega/omega_1,absorber_without,'--',label='without vibration absorber')
plt.ylim([0,17.5])
plt.xlim([0.5,1.5])
plt.legend(framealpha=1)
plt.grid(True)
plt.xlabel(r'$\omega $ / $ \omega_1$')
plt.ylabel(r'$X_1 $ / $\delta_\textnormal{st}$')
plt.xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])

plt.tight_layout(
    pad=0.2,      # overall padding
    w_pad=0.5,    # width padding (between subplots)
    h_pad=0.5,    # height padding (between subplots)
    rect=(0.013, 0, 1, 0.99)  # (left, bottom, right, top)
)
plt.savefig('vibration_absorber_undamped_results',dpi=300)























