"""This code was modified from https://www.youtube.com/watch?v=Kb7mdb5kOpA"""

"""Update: This code is depreciated"""

import numpy as np
from math import sin, pi
from numpy.fft.helper import fftshift
from scipy.linalg import eigh
from numpy.linalg import inv
from matplotlib import pyplot as plt
# from scipy.fft import fft, fftfreq
from numpy.fft import fft, fftfreq 

from tqdm import tqdm

# GLOBAL VARIABLES

F0 = 100.0
k = 4200 # 4160.0
m = 1.82 #1.66
dof = 3

time_step = 1e-4
end_time = 11
time = [round(t,5) for t in np.arange(0, end_time, time_step) ]

# Setting up const matrix & vectors
K = np.array([[2*k,-k,0],[-k,2*k,-k],[0,-k,k]])
M = np.array([[m,0,0],[0,m,0],[0,0,m]])
I = np.identity(dof)
A = np.zeros((2*dof,2*dof))
B = np.zeros((2*dof,2*dof))


# set up B
B[0:3,3:6] = K
B[3:6,0:3] = -I

def sine_sweep(start_omega, end_omega):
    itter_num = end_time/time_step
    omega_step = (end_omega - start_omega)/itter_num
    omegas = []
    omega_temp = start_omega
    for i in range(int(itter_num)):
        omegas.append(omega_temp)
        omega_temp += omega_step
    return omegas

def sine(omega):
    itter_num = end_time/time_step
    omegas = []
    for i in range(int(itter_num)):
        omegas.append(omega)
    return omegas

def init_mass_matrix(delta_m1=0, delta_m2=0, delta_m3=0):
    # setup matrices
    global A
    global M
    M = np.array([[m+delta_m1,0,0],[0,m+delta_m2,0],[0,0,m+delta_m3]])

    # set up A
    A[0:3,0:3] = M
    A[3:6,3:6] = I

def natural_frequency(angular=True):
    # find natural frequencies and mode shapes
    evals, evecs = eigh(K,M)
    frequencies = np.sqrt(evals)
    if not angular:
        frequencies = frequencies/(2 * pi)
    return frequencies, evecs


def get_peak_frequency():
    pass

def main_plot(delta_m1=0, delta_m2=0, delta_m3=0, angular=True, sweep=True, ang_frequency=5, plot=True):
    Y = np.zeros((2*dof,1)) # vector
    F = np.zeros((2*dof,1)) # vector

    init_mass_matrix(delta_m1, delta_m2, delta_m3)

    A_inv = inv(A)
    force = []
    X1 = []
    X2 = []
    X3 = []
    # print("init time array")
    # print(time_step)
    time = [round(t,5) for t in np.arange(0, end_time, time_step)]
    if sweep == True:
        omega = sine_sweep(0, 30*2*pi)
    else:
        omega = sine(ang_frequency)

    # print(len(time))
    # print(len(omega))
    # numerically integrate the EOMs
    for i in range(len(omega)):
    	F[0] = F0 * sin(omega[i]*time[i])
    	Y_new = Y + time_step * A_inv.dot( F - B.dot(Y) )
    	Y = Y_new
    	force.extend(F[0])
    	X1.extend(Y[3])
    	X2.extend(Y[4])
    	X3.extend(Y[5])
    
    # FFT
    # temp_dft = dft(5)
    itter_num = int(end_time/time_step)
    y1f = fft(X1)
    y2f = fft(X2)
    y3f = fft(X3)
    xf = fftfreq(itter_num, time_step)
    mask = xf >= 0
    xf = xf[mask]
    if plot:
        plt.plot(time,X1)
        plt.plot(time,X2)
        plt.plot(time,X3)

        plt.xlabel('time (s)')
        plt.ylabel('displacement (m)')
        plt.title('Response Curves')
        plt.legend(['X1', 'X2', 'X3'], loc='lower right')
        plt.show()

        plt.plot(time,force)
        plt.show()

        plt.plot(xf, 2.0/itter_num * np.abs(y1f[0:itter_num//2])) # dont understand this
        plt.plot(xf, 2.0/itter_num * np.abs(y2f[0:itter_num//2]))
        plt.plot(xf, 2.0/itter_num * np.abs(y3f[0:itter_num//2]))
        # plt.plot(xf, np.abs(y1f))
        # plt.plot(xf,yf)
        plt.show()

    return force, X1, X2, X3


if __name__ == '__main__':
    force, X1, X2, X3 = main_plot(delta_m1=0.1,sweep = True)