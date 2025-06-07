import numpy as np
import matplotlib.pyplot as plt

# Code to represent the graphs of Re(\sigma) vs q.

# Parameters

a=2
d_X=1
d_Y=10
eta=np.sqrt(d_X/d_Y)
b_T=(1+a*eta)**2
b_H=1+a*a
q_T=np.sqrt(a*eta/d_X)
q_H=0
b_c=b_T if b_T<b_H else b_H
q_c=q_T if b_T<b_H else q_H

print(eta,b_T,b_H,q_T,q_H)

# Functions
def tr(b,q):
    return b-1-a*a-q*q*(d_X*d_X+d_Y*d_Y)

def det(b,q):
    return (b-1-q*q*d_X)*(-a*a-q*q*d_Y)+a*a*b

def Delta(b,q):
    return np.lib.scimath.sqrt(tr(b,q)*tr(b,q)-4*det(b,q)) # It can return complex values unlike np.sqrt()

def sigma_p(b,q):
    return 0.5*(tr(b,q)+Delta(b,q))

def sigma_m(b,q):
    return 0.5*(tr(b,q)-Delta(b,q))

def f(b, q):
    return np.maximum(np.real(sigma_p(b,q)), np.real(sigma_m(b,q)))
