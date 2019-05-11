import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.integrate import quad
import os
import csv

###################  Functions  ####################################

##### Compute a first order Bessel integral
def integrand_bessel(tau,x): 
    return cos(tau-x*sin(tau))

def Bessel(x):
    ans, err = quad(integrand_bessel, 0, pi, args=(x))
    answer = ans/pi
    return answer

##### Compute form factor of a rod (R, L) using 1st order Bessel integral
def integrand_rod(alpha,q, R, L):
    a = (2*Bessel(q*R*sin(alpha)))/(q*R*sin(alpha))
    b = sin(q*L*cos(alpha)/2)/(q*L*cos(alpha)/2)
    c = a*b
    return (c**2)*sin(alpha)

def Rodlike(q, R, L):
    ans, err = quad(integrand_rod, 0, 0.5*pi, args = (q, R, L))
    return ans

###### To show and save results 

def automatic_labelling(R, L):
    return "R: {0} nm, L: {1} nm".format(R*1000000000, L*1000000000)

def setting_autosave_string(qL, Sq):
    data = []
    data = zip(qL, Sq)
    with open("autosave.csv","w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(data)
        
    
#####################  Parameters to be adjusted   ##################
# setting wave vectors limit (q0, qn) and the number of step (pas) (not bigger than q0)
q0 = 100000 #10^5
qn = 100000000 #10^8
pas = 100000 #10^5

#Rod dimension in meter
R = 0.000000010 #R:10nm
L = 0.0000007 #L: 700 nm


########## Loop ##################
BOUCLE = True
NUM = 0
print("Software to calculate S(q)=f(qL) of a rod-like system.\n")
while BOUCLE == True:
    NUM += 1

    print("*****************************\nTrial number : ", NUM,"\n")
    R = input("Radius of the rod (nm): ")
    L = input("Length of the rod (nm): ")

    try:
        R = int(R)/1000000000
        L = int(L)/1000000000
    except ValueError:
        print("Please write integer number (without decimal)")

    #Interval
    qL = [q*L for q in range(q0,qn,pas)]

    #Final structur factor
    Sq = [Rodlike(q, R, L) for q in range(q0,qn,pas)]

    ############### quick datasaving ###################################

    setting_autosave_string(qL, Sq)
    print("New data saved in autosave.csv")

    #################### Graphs ########################################

    plt.plot(qL,Sq,"b-", label=automatic_labelling(R, L))

    plt.xscale('log')
    plt.xlabel("q.L")
    plt.yscale('log')
    plt.ylabel("S(q)")

    plt.legend()

    plt.show()



################# other structure factors ##########################
"""

def Gaussian(q,Rg): #structure factor of a gaussian chain
    return 2*(exp(-q*Rg)-1+q*Rg)/(q*Rg*q*Rg)

def Sphere(q,R):
    return (3*(sin(q*R)-q*R*cos(q*R))/(q*R)**3)**2

def Elipse(q,R):
    return (3*(sin(q*R)-q*R*cos(q*R)))/((q*R)**3)

#gaussian chain parameter
Rg=0.000000350 #350 nm

#Sphere
R=0.000000452 #452nm

qRg=[q*Rg for q in range(q0,qn,pas)]

Sq=[Gaussian(q,Rg) for q in range(q0,qn,pas)]
Sq2=[Sphere(q,R) for q in range(q0,qn,pas)]
Sq3=[Elipse(q,R) for q in range(q0,qn,pas)]

"""
