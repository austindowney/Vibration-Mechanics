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
from scipy import fft
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

import numpy, scipy.optimize

def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = numpy.array(tt)
    yy = numpy.array(yy)
    ff = numpy.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(numpy.fft.fft(yy))
    guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = numpy.std(yy) * 2.**0.5
    guess_offset = numpy.mean(yy)
    guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*numpy.pi)
    fitfunc = lambda t: A * numpy.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": numpy.max(pcov), "rawres": (guess,popt,pcov)}




#%% Plot the figure

tt = np.linspace(0,10,10000)   
N = tt.shape[0]
T = tt[1]-tt[0]
Fs = 1/T

DAQ_sample_rate = 5
subsample = np.arange(0,N,int(Fs/DAQ_sample_rate))

omega_1 = 3*np.pi*2
signal_1 = np.sin(omega_1*tt)
omega_2 = omega_1 - (np.pi*2)
A = fit_sin(tt[subsample],signal_1[subsample])
signal_2 = A['amp']*np.sin(A['omega']*tt+A['phase'])









# N = tt.shape[0]
# T = tt[1]-tt[0]
# Fs = 1/T
# xf = sp.fft.fftfreq(N, T)[:N//2]

# signal_2 = 3*np.sin(2*tt) + 1.5*np.sin(4*2*tt) + 1*np.sin(15*tt) #+ 1.5*np.sin(20*tt) #+ 1*np.sin(50*tt)

# fft_signal_1 = 2.0/N * np.abs(sp.fft.fft(signal_1)[0:N//2])
# fft_signal_2 = 2.0/N * np.abs(sp.fft.fft(signal_2)[0:N//2])

# DAQ_sample_rate = 5

# subsample = np.arange(0,100000,int(Fs/DAQ_sample_rate))



plt.figure(figsize=(6.5,3))
plt.plot(tt,signal_1,label='original signal')
plt.plot(tt,signal_2,'--',label='reconstructed signal')
markerline, stemline, baseline, = plt.stem(tt[subsample],signal_2[subsample],'ko',markerfmt='ko', label='signal digitization')
plt.setp(stemline, linewidth = 1.5)
plt.setp(markerline, markersize = 6)
plt.xlim([0,1])
plt.grid(True)
plt.ylabel('$x(t)$')
plt.xlabel('time (s)')
plt.legend(framealpha=1,loc=4)
plt.tight_layout()


plt.savefig('aliasing',dpi=500)


















