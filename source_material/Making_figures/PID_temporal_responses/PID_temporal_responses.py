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



#%% 
# %% 1-DOF mass–spring–damper with basic PID (for-loop, minimal)

import numpy as np
import matplotlib.pyplot as plt

# --------------------------- PARAMETERS ------------------------------------- #
# Plant
m = 1.0     # kg
c = 0.6     # N·s/m
k = 50.0    # N/m

# PID gains
Kp = 120.0
Ki = 300.0
Kd = 3.0

# Reference: step of size r_final at step_time
r_final  = 1.0
step_time = 1.0   # s

# Simulation
t_final = 10.0    # s
wn = np.sqrt(k/m)
dt = min(1.0/(200*wn), 1e-3)  # small stable step
N = int(np.round(t_final/dt)) + 1
t = np.linspace(0.0, t_final, N)

# --------------------------- STATE ARRAYS ----------------------------------- #
x  = np.zeros(N)   # position
xd = np.zeros(N)   # velocity
z  = np.zeros(N)   # integral of error
u  = np.zeros(N)   # control force
rtr= np.zeros(N)   # reference trace

# --------------------------- TIME-STEP LOOP --------------------------------- #
for i in range(N-1):
    # reference (delayed step)
    r = r_final if t[i] >= step_time else 0.0
    rtr[i] = r

    # error and its derivative (use rdot=0 to avoid derivative kick)
    e    = r - x[i]
    edot = 0.0 - xd[i]

    # PID control
    u[i] = Kp*e + Ki*z[i] + Kd*edot

    # plant dynamics: ẍ = (u - c ẋ - k x)/m
    xdd = (u[i] - c*xd[i] - k*x[i]) / m

    # integrate (semi-implicit Euler)
    xd[i+1] = xd[i] + dt*xdd
    x[i+1]  = x[i] + dt*xd[i+1]
    z[i+1]  = z[i] + dt*e

# last samples for plotting
rtr[-1] = r_final if t[-1] >= step_time else 0.0
u[-1] = u[-2]

# --------------------------- PLOTS ------------------------------------------ #
plt.rcParams.update({"font.family": "Times New Roman", "figure.dpi": 130})

plt.figure(figsize=(6.5, 3.5))

plt.subplot(211)
plt.plot(t, rtr, label="step input")
plt.plot(t, x,  "--", label="system response")
plt.xlabel("time (s)\n(a)")
plt.yticks([0,0.5,1,1.5])
plt.ylim([-0.1,1.6,])
plt.xlim([0,6])
plt.ylabel("displacement (m)")
plt.grid(True, alpha=0.35)
plt.legend(loc="lower right", framealpha=1)


plt.subplot(212)
plt.plot(t, u)
plt.xlim([0,6])
plt.yticks([-50,0,50,100,150])

plt.xlabel("time (s)\n(b)")
plt.ylabel("control force $u$ (N)")
plt.grid(True, alpha=0.35)


plt.tight_layout()
plt.savefig('PID_temporal_responses.png',dpi=300)
    
    





















































































