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


