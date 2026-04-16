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

tt = np.linspace(0,100,100000)   

signal_1 = 5.3*np.sin(2*tt)

N = tt.shape[0]
T = tt[1]-tt[0]
Fs = 1/T
xf = sp.fft.fftfreq(N, T)[:N//2]

signal_2 = 3*np.sin(2*tt) + 1.5*np.sin(4*2*tt) + 1*np.sin(15*tt) #+ 1.5*np.sin(20*tt) #+ 1*np.sin(50*tt)

fft_signal_1 = 2.0/N * np.abs(sp.fft.fft(signal_1)[0:N//2])
fft_signal_2 = 2.0/N * np.abs(sp.fft.fft(signal_2)[0:N//2])

DAQ_sample_rate = 5

subsample = np.arange(0,100000,int(Fs/DAQ_sample_rate))



plt.figure(figsize=(6.5,3))
plt.subplot(2,3,1)
plt.plot(tt,signal_1)
plt.xlim([0,5])
plt.grid(True)
plt.ylabel('$x(t)$')
plt.tight_layout()
plt.title('Signal')

plt.subplot(2,3,2)
markerline, stemline, baseline, = plt.stem(tt[subsample],signal_1[subsample])
plt.setp(stemline, linewidth = 0.75)
plt.setp(markerline, markersize = 3)
plt.xlim([0,5])
plt.grid(True)
plt.ylabel('$x(t)$')
plt.tight_layout()
plt.title('Digitized Signal')

plt.subplot(2,3,3)
plt.plot(xf,fft_signal_1)
plt.xlim([0,3])
plt.grid(True)
plt.ylabel('PSD')
plt.tight_layout()
plt.title('Signal Frequencies')

plt.subplot(2,3,4)
plt.plot(tt,signal_2)
plt.xlim([0,5])
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('$x(t)$')
plt.tight_layout()


plt.subplot(2,3,5)
markerline, stemline, baseline, = plt.stem(tt[subsample],signal_2[subsample])
plt.setp(stemline, linewidth = 0.75)
plt.setp(markerline, markersize = 3)
plt.xlim([0,5])
plt.grid(True)
plt.ylabel('$x(t)$')
plt.xlabel('time (s)')
plt.tight_layout()


plt.subplot(2,3,6)
plt.plot(xf,fft_signal_2)
plt.xlim([0,3])
plt.grid(True)
plt.xlabel('frequency (Hz)')
plt.ylabel('PSD')
plt.tight_layout()


plt.savefig('signal_digitization',dpi=300)


















