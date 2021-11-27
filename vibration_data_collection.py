"""This script is too slow so depreciated"""

import mdof_vibrations as mv
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from math import pi

def sfl(t,x,omega):
    # slow fourier lol
    # input a list of t, a list of displacement x, and analyze it at a angular frequency omega
    # returns the frequency and the amplitude at that frequency
    a=0
    b=0
    s=0
    c=0
    for i in range(len(t)):
        a+=np.sin(omega*t[i])*x[i]
        s+=np.sin(omega*t[i])**2        
        b+=np.cos(omega*t[i])*x[i]
        c+=np.cos(omega*t[i])**2
    X=((a/s)**2+(b/c)**2)**0.5
    return (X)

mv.init_mass_matrix()
frequencies, evecs = mv.natural_frequency(angular=False)
print(frequencies)
print(evecs)

omega = 1

omegas = []
amp = []

for i in tqdm(range(2000)):
    force, x3, x2, x1 = mv.main_plot(plot=False, sweep=False, ang_frequency=omega)
    omegas.append(omega/(2*pi))
    amp.append(sfl(mv.time, x3, omega))
    omega += (1/100)

plt.plot(omegas, amp)
plt.show()

