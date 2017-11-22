# in ipython notebook, enable inline plotting with:
# %pylab inline --no-import-all
import matplotlib.pyplot as plt

# create some circles
#circle1 = plt.Circle((-.5,0), 1.5, color='r', alpha=.5)
#circle2 = plt.Circle(( .5,0), 1, color='b', alpha=.5)

plot_receiver1 = plt.Circle((1.55,17.63), 10, color = 'r', alpha = .5)
plot_receiver2 = plt.Circle((-4.02,0), 10, color = 'b', alpha = .5)
plot_receiver3 = plt.Circle((-4.4, 9.6), 10, color = 'g', alpha = .5)
plot_receiver4 = plt.Circle((9.27,4.64), 10, color = 'c', alpha = .5)
plot_receiver5 = plt.Circle((9.15,12.0), 10, color = 'm', alpha = .5)

# add them to the plot (bad form to use ;, but saving space)
# and control the display a bit
ax = plt.gca()
ax.add_artist(plot_receiver1)
ax.add_artist(plot_receiver2)
ax.add_artist(plot_receiver3)
ax.add_artist(plot_receiver4)
ax.add_artist(plot_receiver5)
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
#ax.set_aspect('equal')

# display it
plt.plot()
plt.show()