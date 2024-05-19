
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




#%% Plot data

file_name = 'comfort_2'
with open('data/'+file_name+'.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)
comfort_frequencies = loaded_dict['frequencies']
comfort_psd = loaded_dict['psd']

file_name = 'comfort_2'
D1 = np.loadtxt('data/'+file_name+'.lvm',skiprows=23,max_rows=16000,delimiter='\t')
comfort_tt = D1[:,0]
comfort_aa = D1[:,1]

file_name = 'normal_2'
with open('data/'+file_name+'.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)
normal_frequencies = loaded_dict['frequencies']
normal_psd = loaded_dict['psd']

file_name = 'normal_2'
D1 = np.loadtxt('data/'+file_name+'.lvm',skiprows=23,max_rows=16000,delimiter='\t')
normal_tt = D1[:,0]
normal_aa = D1[:,1]

file_name = 'sport_2'
with open('data/'+file_name+'.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)
sport_frequencies = loaded_dict['frequencies']
sport_psd = loaded_dict['psd']

file_name = 'sport_2'
D1 = np.loadtxt('data/'+file_name+'.lvm',skiprows=23,max_rows=16000,delimiter='\t')
sport_tt = D1[:,0]
sport_aa = D1[:,1]

plt.subplots(figsize=(6, 2.5))
plt.xlim([0,5])
plt.plot(sport_frequencies, sport_psd,':',label='sport')
plt.plot(normal_frequencies, normal_psd,'--',label='normal')
plt.plot(comfort_frequencies, comfort_psd,label='comfort')
plt.xlabel("frequency (Hz)")
plt.ylabel('power spectral density\n[m$^2$/(s$^4 \cdot$ Hz)]')
plt.legend(framealpha=1)
# ax1.set_ylim([0,0.003])
# ax2.set_ylim([0,0.000009])
plt.tight_layout()

plt.savefig('data_plot.pdf')
plt.savefig('VW_GTI_Suspension_2.jpg',dpi=250)

linew = 0.8

plt.figure(figsize=(6, 4.0))
plt.subplot(211)
plt.xlim([0,2])
plt.grid('on')
plt.plot(sport_tt, sport_aa,':',lw=0.9,label='sport',zorder=3)
plt.plot(normal_tt, normal_aa,'--',lw=0.75,label='normal',zorder=2)
plt.plot(comfort_tt, comfort_aa,lw=0.6,label='comfort',zorder=1)
plt.xlabel("time (s)\n(a)")
plt.ylabel('acceleraction (m/s$^2$)')


leg = plt.legend(framealpha=1,ncol=3,loc=4)
for line in leg.get_lines():
    line.set_linewidth(1.2)
#plt.legend(framealpha=1,ncol=3,loc=4)

linew = 1.5

plt.subplot((212))
plt.xlim([0,5])
plt.plot(sport_frequencies, sport_psd,':',lw=linew,label='sport')
plt.plot(normal_frequencies, normal_psd,'--',lw=linew,label='normal')
plt.plot(comfort_frequencies, comfort_psd,lw=linew,label='comfort')
plt.xlabel("frequency (Hz)\n(b)")
plt.ylabel('power spectral density\n(m$^2$/[s$^4 \cdot$ Hz])')
#plt.legend(framealpha=1)
# ax1.set_ylim([0,0.003])
# ax2.set_ylim([0,0.000009])
plt.tight_layout()

plt.savefig('data_plot.pdf')
plt.savefig('VW_GTI_Suspension_2.jpg',dpi=300)


























