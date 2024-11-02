import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy as sp
import numpy as np

mpl.rcParams['text.color'] = 'white'
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['xtick.color'] = 'white' 
mpl.rcParams['axes.edgecolor'] = 'white' 
mpl.rcParams['ytick.color'] = 'white'

x = np.arange(0, 21, dtype=np.float64)
gamma_y = sp.special.gamma(x)
ramsey_y = 2.**(x**2)
exp_y = 2**(x)
cmap = sns.color_palette("Set2")

plt.plot(x, ramsey_y, c=cmap[0], label=r'$2^{n^2}$')
plt.plot(x, gamma_y, c=cmap[1], label=r'$\Gamma(n)$')
plt.plot(x, exp_y, c=cmap[2], label=r'$2^n$')

plt.gcf().patch.set_facecolor('#1b1b1b')
plt.gca().patch.set_facecolor('#1b1b1b')

legend = plt.legend()
frame = legend.get_frame()
frame.set_facecolor('#1b1b1b')

plt.xlabel(r'$n$')
plt.xticks(x[::5])
plt.ylabel(r'$f(n)$')
plt.yscale('log')
plt.savefig('results/visualizations/large_function_growth.pdf')