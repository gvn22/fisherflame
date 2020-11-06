import h5py
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

f = h5py.File('./analysis_tasks/analysis.h5','r')
x = f['/scales/x/1.0'][:]
t = f['/scales/sim_time'][:]
s = f['/tasks/s'][:]
r = f['/tasks/r'][:]
c = f['/tasks/c'][:]
f.close()

p = Path('figures/')
p.mkdir(exist_ok=True)

print('Creating and saving figures...')

fig,ax = plt.subplots()
plt.plot(t,s)
plt.ylabel(r'$s$')
plt.xlabel(r'$t$')
plt.savefig('figures/s_profile.png',format='png')

fig,ax = plt.subplots()
plt.plot(x,r[0],label=r'$t = 0$')
plt.plot(x,r[-1],label=r'$t = 100$')
plt.ylabel(r'$\dot{\omega}$')
plt.xlabel(r'$x$')
plt.legend(loc=2)
plt.savefig('figures/r_profile.png',format='png')

fig,ax = plt.subplots()
plt.plot(x,c[0],label=r'$t = 0$')
plt.plot(x,c[-1],label=r'$t = 100$')
plt.ylabel(r'$c$')
plt.xlabel(r'$x$')

plt.legend(loc=2)
plt.savefig('figures/c_profile.png',format='png')
