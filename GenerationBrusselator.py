import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import matplotlib as mpl
mpl.rcParams['animation.embed_limit'] = 50 #to be able to produce heavy animations (long simulations)

#Parameters
a=2
d_X=1
d_Y=5

eta=np.sqrt(d_X/d_Y)
b_T=(1+a*eta)**2
b_H=1+a*a
b_c=b_T if b_T<b_H else b_H
instability="Turing" if b_T<b_H else "Hopf"

b=b_c*1.2

#Discretization
L=100 #simulation size
N=100 #spacial discretization
dx=dy=L/N

T=40 #simulation time
dt=0.01
steps=int(T/dt)

#animation parameters
spf=int(0.1/dt) #steps per frame (to show 0.1 units of time per frame)
fps=30 #frames per second of simulation (controls animation speed)
save_to_file=False
filename=f"brusselator_{instability}_{b_c:.2f}_{a}_{d_X}_{d_Y}_{b/b_c:.2f}bc"

#Initialize concentrations: stead_Y state plus random noise
x=np.clip(a+0.1*np.random.randn(N, N),0,None)
y=np.clip(b/a+0.1*np.random.randn(N, N),0,None)

#Figure and axis for the animation
fig, ax=plt.subplots(figsize=(5, 5))

vmin=np.min(x)
vmax=np.max(x)
extent=[0,L,0,L]

imx=ax.imshow(x,cmap='rainbow',vmin=vmin,vmax=vmax,extent=extent,origin='lower')
ax.set_title('x concentration')

#Add colorbar
cbar=fig.colorbar(imx,ax=ax,shrink=0.8)
cbar.set_label("x concentration")

#Discrete Laplacian with periodic boundary conditions
def laplacian(u):
    down=np.roll(u,1,axis=0) #down[i,j]=u[i+1,j] for 0<=i<=N-2, down[N-1,j]=u[0,j]
    up=np.roll(u,-1,axis=0) #up[i,j]=u[i-1,j] for 1<=i<=N-1, up[0,j]=u[N-1,j]
    right=np.roll(u,1,axis=1) #right[i,j]=u[i,j+1] for 0<=j<=N-2, righ[i,N-1]=u[i,0]
    left=np.roll(u,-1,axis=1) #left[i,j]=u[i,j-1] for 1<=j<=N-1, left[i,0]=u[i,N-1]
    return (down+up+right+left-4*u)/dx**2

#initialize the animation with the initial condition
def init():
    imx.set_data(x)
    return [imx]

#update function to simulate the system
def update(frame):
  global x, y
  for _ in range(spf):
      dxdt=a-(b+1)*x+x*x*y+d_X*laplacian(x)
      dydt=b*x-x*x*y+d_Y*laplacian(y)

      x+=dt*dxdt
      y+=dt*dydt

  imx.set_data(x)
  ax.set_title(f"time: {frame*spf*dt:.2f}")
  return [imx]

#produce animation
anim=FuncAnimation(fig,update,frames=round(steps/spf),init_func=init,interval=1000/fps,blit=True)
plt.close()

#Saving/showing the animation
if save_to_file:
    anim.save(f"{filename}.mp4", dpi=150)
else:
    display(HTML(anim.to_jshtml()))
