import numpy
import cubic_solver as cs
from math import sqrt, pi
from matplotlib import pyplot as plt
from numpy import sort as sort_array

# GLOBAL
k = 4200 # 4160.0
m = 1.83 # 1.66

def get_omega(a_list):
    omega_list = list()
    for a in a_list:
        omega = sqrt(a*k/m)/(2*pi)
        omega_list.append(omega)
    return omega_list

def theoretical_analysis(lambda_number=1, plot=True):
    mass = []
    frequency1 = []
    frequency2 = []
    frequency3 = []


    intervals = 0.01
    if lambda_number==1: # change top mass
        ld1 = 1
        ld2 = 1 + 0.5/m
        ld3 = 1 + 0.5/m
    elif lambda_number==2: # change middle top mass
        ld1 = 1 + 0.5/m
        ld2 = 1
        ld3 = 1 + 0.5/m
    elif lambda_number==3: # change bottom mass
        ld1 = 1 + 0.5/m
        ld2 = 1 + 0.5/m
        ld3 = 1
    elif lambda_number==4: # change all mass
        ld1 = 1
        ld2 = 1
        ld3 = 1
    else:
        print("please select value 1, 2, 3, 4")

    for _ in range(100):
        a=(ld1 * ld2 * ld3)
        b=-(2*ld1*ld2 + 2*ld1*ld3 + ld2*ld3)
        c=(3*ld1 + 2*ld2 + ld3)
        d=-1

        if lambda_number==1:
            mass.append(m*ld1)
            ld1 += intervals/m
        elif lambda_number==2:
            mass.append(m*ld2)
            ld2 += intervals/m
        elif lambda_number==3:
            mass.append(m*ld3)
            ld3 += intervals/m
        else:
            mass.append(m*ld1)
            ld1 += intervals/m
            ld2 += intervals/m
            ld3 += intervals/m

        omegas = sort_array(get_omega(cs.solve(a, b, c, d)))
        frequency1.append(omegas[0])
        frequency2.append(omegas[1])
        frequency3.append(omegas[2])

    frequencies = [frequency1, frequency2, frequency3]
    if plot:
        for i in range(len(frequencies)):
            frequency = frequencies[i]
            plt.xlabel('mass (kg)')
            plt.ylabel('Natural frequency {0} (Hz)'.format(i+1))
            plt.title('Natural frequency against mass')
            plt.plot(mass, frequency)
            plt.show()
    
    return mass, frequencies

if __name__ == '__main__':
    print(len(theoretical_analysis(lambda_number=1, plot=False)[1]))
    # theoretical_analysis(lambda_number=2)
    # theoretical_analysis(lambda_number=3)
    # theoretical_analysis(lambda_number=4)