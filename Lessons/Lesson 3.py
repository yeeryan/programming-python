# Visualizing Tabular Data

import matplotlib.pyplot
import numpy as np

# Data import (from lesson 2)
data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

# Basic Visual of "Data"
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()

# Average inflammation over time
avg_inflammation = np.mean(data, axis=0)
avg_plot = matplotlib.pyplot.plot(avg_inflammation)
matplotlib.pyplot.show()

# Max inflammation
max_plot = matplotlib.pyplot.plot(np.max(data, axis=0))

min_plot = matplotlib.pyplot.plot(np.min(data, axis=0))

# Grouping Plots
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
̇
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.mean(data, axis=0))

axes3.set_ylabel('min')
axes3.set_ylim(0, 6)
axes3.plot(np.mean(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig('inflammation.png')
matplotlib.pyplot.show()

# std plot

std_plot = matplotlib.pyplot.plot(np.std(data, axis=0))

matplotlib.pyplot.show()
