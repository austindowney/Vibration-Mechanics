#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:30:27 2016

@author: downey
"""

#%% import modules and set default fonts and colors

import IPython as IP
IP.get_ipython().magic('reset -sf')
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
plt.rcParams.update({'image.cmap': 'viridis'})
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
 'Century Schoolbook L',  'Utopia', 'ITC Bookman', 'Bookman', 
 'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.fontset': 'custom'})
plt.close('all')


#%% response_to_random_input_inputs

tt = np.linspace(0,1000,50000)

xx_sin = np.sin(tt)
xx_rand = (np.random.rand(tt.shape[0])-0.5)*2




plt.figure(figsize=(6.5,3))
plt.subplot(121)
plt.plot(tt,xx_sin)
plt.ylabel('x')
plt.xlabel('time (s)')
plt.grid('on')
plt.xlim(0,10)
plt.ylim(-1.1,1.1)
#plt.title('sinusoidal loading')

plt.subplot(122)
plt.plot(tt,xx_rand)
plt.ylabel('x')
plt.xlabel('time (s)')
plt.grid('on')
plt.xlim(0,10)
plt.ylim(-1.1,1.1)
#plt.title('uniform random noise')
plt.tight_layout()
plt.savefig('response_to_random_input_inputs',dpi=300)


#%% response_to_random_input_autocorrelation


def estimated_autocorrelation(x):
    """
    http://stackoverflow.com/q/14297012/190597
    http://en.wikipedia.org/wiki/Autocorrelation#Estimation
    """
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = np.correlate(x, x, mode = 'full')[-n:]
    assert np.allclose(r, np.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(variance*(np.arange(n, 0, -1)))
    return result

R_xx_sin = estimated_autocorrelation(xx_sin)   
R_xx_rand = estimated_autocorrelation(xx_rand)  

plt.figure(figsize=(6.5,3))
plt.subplot(121)
plt.plot(tt,R_xx_sin)
plt.ylabel('$R_{xx}$')
plt.xlabel(r'time shift $\tau$ (s)')
plt.grid('on')
plt.xlim(0,10)
plt.ylim(-1.1,1.1)
#plt.title('sinusoidal loading')

plt.subplot(122)
plt.plot(tt,R_xx_rand,label='calculated')
plt.plot(tt[0:2],R_xx_rand[0:2],'-',color=cc[0],linewidth=5)
plt.plot([0.1,0.1],[0,1],'--',color='red',linewidth=2,label='theoretical')
plt.ylabel('$R_{xx}$')
plt.xlabel(r'time shift $\tau$ (s)')
plt.grid('on')
plt.xlim(0,10)
plt.ylim(-1.1,1.1)
#plt.title('uniform random noise')
plt.tight_layout()
plt.legend(framealpha=1)
plt.savefig('response_to_random_input_autocorrelation',dpi=300)



#%% response_to_random_input_PSD

from scipy.fftpack import fft

def Fourier_transform(tt,xx):
    # Number of sample points
    N = xx.shape[0]
    # sample spacing
    T = tt[1]-tt[0]
    x = np.linspace(0.0, N*T, N)
    fft_y = fft(xx)
    yf =  2.0/N * np.abs(fft_y[0:N//2])
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    return(xf,yf)


[PSD_xx_sin,PSD_yy_sin] = Fourier_transform(tt,R_xx_sin)
[PSD_xx_rand,PSD_yy_rand] = Fourier_transform(tt,R_xx_rand)




plt.figure(figsize=(6.5,3))
plt.subplot(121)
plt.plot(PSD_xx_sin,PSD_yy_sin)
plt.ylabel('PSD')
plt.xlabel('Frequency (Hz)')
plt.grid('on')
plt.xlim(0,1)
#plt.ylim(-1.1,1.1)
plt.title('sinusoidal loading')

plt.subplot(122)
plt.plot(PSD_xx_rand,PSD_yy_rand,label='calculated')
plt.plot([0,1],[np.mean(PSD_yy_rand),np.mean(PSD_yy_rand)],'--',color='red',linewidth=2,label='theoretical')
plt.ylabel('PSD')
plt.xlabel('Frequency (Hz)')
plt.grid('on')
plt.xlim(0,1)
#plt.ylim(-1.1,1.1)
plt.title('uniform random noise')
plt.tight_layout()
plt.legend(framealpha=1)
plt.savefig('response_to_random_input_PSD_python.pdf')


















