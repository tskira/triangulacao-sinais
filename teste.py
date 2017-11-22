import numpy as np 
import matplotlib.pyplot as plt
import math 

receiver = ((-3.99, 0.0, 1.35, -26.0, 2.1), (5.55, 1.28, 1.35, -33.8, 1.8), (0.35, -6.94, 1.35, -29.8, 1.3), (0.16, 7.35, 1.35, -31.2, 1.4), (-7.35, 4.55, 1.35, -33.0, 1.5))
r = np.matrix([[4.1],[5.5],[7.7],[6.5],[8.3]])

def dk(potency_k):
    for i in range(5):
        r[i,0] = (math.pow(10.0, ((receiver[i][3] - potency_k[i]) / (10.0 * receiver[i][4]))))

def const_factor(receiver_number):
    return(math.pow(receiver[receiver_number][0], 2) + math.pow(receiver[receiver_number][1], 1))

def mmq(receiver_position):
    a = np.matrix([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
    b = np.matrix([[0.0],[0.0],[0.0],[0.0]])
    #dk(receiver_position)
    x0 = receiver[0][0]
    y0 = receiver[0][1]
    for i in range(4):
        a[i,0] = receiver[i][0] - x0
        a[i,1] = receiver[i][1] - y0
        b[i,0] = -(x0*x0) -(y0*y0) + (r[0]*r[0]) + (receiver[i][0]*receiver[i][0]) + (receiver[i][1]*receiver[i][1]) - (r[i]*r[i])     
    
    a = 2 * a
    return (np.linalg.inv(a.transpose() * a) * a.transpose() * b)

read_position = tuple(map(float, input().split()))
resp = mmq(read_position)
print(r)

''' plot no grafico '''

plot_receiver1 = plt.Circle((-3.99, 0.0), r[0], color = 'r', alpha = .6)
plot_receiver2 = plt.Circle((5.55, 1.28),  r[1], color = 'b', alpha = .6)
plot_receiver3 = plt.Circle((0.35, -6.94),  r[2], color = 'm', alpha = .6)
plot_receiver4 = plt.Circle((0.16, 7.35),  r[3], color = 'y', alpha = .6)
plot_receiver5 = plt.Circle((-7.35, 4.55),  r[4], color = 'k', alpha = .6)
plt.plot([3.0], [3.0], 'go')
plt.plot([resp[0,0]], [resp[1,0]], 'ro')
ax = plt.gca()
ax.add_artist(plot_receiver1)
ax.add_artist(plot_receiver2)
ax.add_artist(plot_receiver3)
ax.add_artist(plot_receiver4)
ax.add_artist(plot_receiver5)
ax.set_xlim(-30, 30)
ax.set_ylim(-30 ,30)
plt.plot()
plt.show()
print(resp)