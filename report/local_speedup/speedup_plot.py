# plotter for speedup
import numpy as np
import matplotlib.pyplot as plt

cores = np.array([1, 2, 5, 10, 20, 26])
tot_filters = 75
runtime = np.array([881.723, 558.624, 288.268, 162.4102, 95.5782, 55.0291])
serial = runtime[0]


plt.figure(1)
plt.plot(cores, runtime / tot_filters, 'midnightblue')
plt.xlabel('Number of Cores')
plt.ylabel('Time per Filter (s)')

plt.savefig('time_per_filter.png', dpi=250)
plt.close()

plt.figure(2)
plt.plot(cores, serial / runtime, 'darkgreen')
plt.xlabel('Number of Cores')
plt.ylabel('Speedup')

plt.savefig('speedup.png', dpi=250)
plt.close()
