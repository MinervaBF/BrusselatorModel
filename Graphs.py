import numpy as np
import matplotlib.pyplot as plt

#parameters
a=2
d_X=1
d_Y=2
eta=np.sqrt(d_X/d_Y)
eta_0=(np.sqrt(1+a*a)-1)/a

b_T=(1+a*eta)**2
b_H=1+a*a
q_T=np.sqrt(a*eta/d_X)
q_H=0
b_c=b_T if b_T<b_H else b_H
q_c=q_T if b_T<b_H else q_H

save_to_file=False
instability="Turing" if b_T<b_H else "Hopf"
filename=f"brusselator_{instability}_{b_c:.2f}_{a}_{d_X}_{d_Y}"

print(eta,eta_0,b_c,q_c,b_T,b_H,q_T,q_H)

#functions
def tr(b,q):
    return b-1-a*a-q*q*(d_X*d_X+d_Y*d_Y)

def det(b,q):
    return (b-1-q*q*d_X)*(-a*a-q*q*d_Y)+a*a*b

def Delta(b,q):
    return np.lib.scimath.sqrt(tr(b,q)*tr(b,q)-4*det(b,q)) #it can return complex values unlike np.sqrt()

def sigma_p(b,q):
    return 0.5*(tr(b,q)+Delta(b,q))


q = np.linspace(0, 3, 500)

fig, ax = plt.subplots()

y1 = np.real(sigma_p(0.8*b_c, q))
y2 = np.real(sigma_p(b_c, q))
y3 = np.real(sigma_p(1.2*b_c, q))

mask1=(y1>=-10)
mask2=(y2>=-10)
mask3=(y3>=-10)

ax.plot(q[mask1], y1[mask1], label=r'$b=0.8b_c$')
ax.plot(q[mask2], y2[mask2], label=fr'$b=b_c={b_c:.2f}$')
ax.plot(q[mask3], y3[mask3], label=r'$b=1.2b_c$')

plt.axvline(x=q_c,color='black',linestyle='--',label=fr'$q = q_c={q_c:.2f}$')

plt.xlabel(r'$q$',loc='right')
plt.ylabel(r'$\Re(\sigma_q^+)$',loc='top')

#Make axes cross at (0,0)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

#Hide top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.legend(loc='lower center')

if save_to_file:
    plt.savefig(f"{filename}.png")
else:
    plt.show()



