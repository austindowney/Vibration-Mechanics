# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import modules
import IPython as IP
IP.get_ipython().magic('reset -sf')

import warnings     # added to ignore the plotting warings about font types in math mode
warnings.simplefilter("ignore", UserWarning)

import matplotlib as mpl
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import os as os
import numpy as np
import scipy as sp
import copy as copy
from matplotlib import cm
import time
#import pykrige as pykrige
import scipy.io as sio
tt1 = time.time()

plt.close('all')



#%% Problem 3


tt = np.linspace(-62,62,1000)

plt.figure(figsize=(6,3))
plt.plot(tt,np.arctan(tt))



plt.grid('on')
plt.ylabel('$y$')
plt.gca().set_yticklabels(['$\dfrac{-\pi}{2}$','$\dfrac{-\pi}{4}$',0,'$\dfrac{\pi}{4}$','$\dfrac{\pi}{2}$'])
plt.yticks([-np.pi/2,-np.pi/4,0,np.pi/4,np.pi/2])
plt.xlim([-61,61])
plt.xlabel('$x$')
plt.tight_layout()
plt.savefig('arctan_plot',dpi=300)













































































