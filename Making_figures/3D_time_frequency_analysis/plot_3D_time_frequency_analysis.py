#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Default plotting code for Open_Vibrations that sets the fonts and format.

@author: Austin Downey
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
from matplotlib.patches import Circle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d


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
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D


def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    '''
    Plots the string 's' on the axes 'ax', with position 'xyz', size 'size',
    and rotation angle 'angle'.  'zdir' gives the axis which is to be treated
    as the third dimension.  usetex is a boolean indicating whether the string
    should be interpreted as latex or not.  Any additional keyword arguments
    are passed on to transform_path.

    Note: zdir affects the interpretation of xyz.
    '''
    x, y, z = xyz
    if zdir == "y":
        xy1, z1 = (x, z), y
    elif zdir == "x":
        xy1, z1 = (y, z), x
    else:
        xy1, z1 = (x, y), z

    text_path = TextPath((0, 0), s, size=size, usetex=usetex)
    trans = Affine2D().rotate(angle).translate(xy1[0], xy1[1])

    p1 = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p1)
    art3d.pathpatch_2d_to_3d(p1, z=z1, zdir=zdir)

plt.close('all')

#%% make the data






tt = np.linspace(0,10,num=200)
frequency = np.linspace(0,4,num=200,endpoint=False)
frequency_A = np.ones(tt.shape[0])*0

f = 0.5
A=0.25
freq_1 = A*np.sin(f*2*np.pi*tt)
data_1 = np.vstack((tt, np.ones(tt.shape[0])*3,freq_1)).T
frequency_A[frequency==3]=A

f = 0.25
A=0.5
freq_2 = A*np.sin(f*2*np.pi*tt)
data_2 = np.vstack((tt, np.ones(tt.shape[0])*2,freq_2)).T
frequency_A[frequency==2]=A

f = 0.1
A=1
freq_3 = A*np.sin(f*2*np.pi*tt)
data_3 = np.vstack((tt, np.ones(tt.shape[0])*1,freq_3)).T
frequency_A[frequency==1]=A

frequency_A = frequency_A*1.8-1.1

time = np.sum((data_1[:,2],data_2[:,2],data_3[:,2]),axis=0)
data_time = np.vstack((tt, np.ones(tt.shape[0])*-0.5,time)).T



# # Number of sample points
# N = tt.shape[0]
# # sample spacing
# T = 1.0 / N
# yf = sp.fft.fft(time)
# xf = sp.fft.fftfreq(N, T)[:N//2]
# yf = 2.0/N * np.abs(yf[0:N//2])

                    
# plt.plot(xf, yf)
# plt.grid()
# plt.show()






#%% Make the figure


plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(data_1[:,0],data_1[:,1],data_1[:,2])
ax.plot3D(data_2[:,0],data_2[:,1],data_2[:,2])
ax.plot3D(data_3[:,0],data_3[:,1],data_3[:,2])
ax.plot3D(data_time[:,0],data_time[:,1],data_time[:,2])
ax.plot3D(np.ones(tt.shape[0])*11.5, frequency,frequency_A)

ax.grid(False)
ax.set_axis_off()





p = mpl.patches.Rectangle((-0.25, -1.8), 10.5,3.0,alpha=0.5,color='gray')
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=-0.5, zdir="y")



p = mpl.patches.Rectangle((-0, -1.8), 4,3.0,alpha=0.5,color='gray')
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=11.5, zdir="x")


p = mpl.patches.Arrow(5,-1.5,0,1.0,width=6)#,color='gray')
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=-1.8, zdir="z")



p = mpl.patches.Arrow(13.75,2,-2.25,0,width=3)#,color='gray')
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=-1.8, zdir="z")




text3d(ax, (2.75, -2.25, -1.8),
       r"time domain (s)",
       zdir="z", size=0.8, usetex=False,
       ec="none", fc="k")




text3d(ax, (15, 0.5, -1.8),
       r"frequency",
       zdir="z", size=0.8, usetex=False,angle=1.5708,
       ec="none", fc="k")
text3d(ax, (16, 0.3, -1.8),
       r"domain (hz)",
       zdir="z", size=0.8, usetex=False,angle=1.5708,
       ec="none", fc="k")




ax.view_init(elev=48, azim=-48, roll=0)
ax.dist = 13

plt.savefig('python.pdf')

# # Demo 1: zdir
# zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
# xs = (1, 4, 4, 9, 4, 1)
# ys = (2, 5, 8, 10, 1, 2)
# zs = (10, 3, 8, 9, 1, 8)

# for zdir, x, y, z in zip(zdirs, xs, ys, zs):
#     label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
#     ax.text(x, y, z, label, zdir)

# Demo 2: color
#ax.text(-10, 2, 0, "red", color='red')

# # Demo 3: text2D
# # Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
# ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)

# # Tweaking display region and labels
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# ax.set_zlim(0, 10)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')





































