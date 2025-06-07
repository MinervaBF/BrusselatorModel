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

q = np.linspace(0, 1, 500)

fig, ax = plt.subplots()

y1 = np.real(sigma_p(0.6*b_c, q))
y2 = np.real(sigma_p(b_c, q))
y3 = np.real(sigma_p(1.4*b_c, q))
y4 = np.real(sigma_p(1.8*b_c, q))

mask1=(y1>=-10)
mask2=(y2>=-10)
mask3=(y3>=-10)
mask4=(y4>=-10)

ax.plot(q[mask1], y1[mask1], label=r'$b=0.6b_c$')
ax.plot(q[mask2], y2[mask2], label=r'$b=b_c$')
ax.plot(q[mask3], y3[mask3], label=r'$b=1.4b_c$')
ax.plot(q[mask4], y4[mask4], label=r'$b=1.8b_c$')

plt.axvline(x=q_c, color='black', linestyle='--', label=r'$q = q_c$')

plt.xlabel(r'$q$', loc='right')
plt.ylabel(r'$\Re(\sigma_q^+)$',rotation=0, loc='top', labelpad=-20)

#Make axes cross at (0,0)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

#Hide top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.legend()

plt.show()

