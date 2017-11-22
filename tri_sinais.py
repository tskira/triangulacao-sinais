import numpy as np 
import matplotlib.pyplot as plt
import math 

receiver = ((1.55, 17.63, 1.35, -26.0, 2.1), (-4.02, 0.0, 1.35, -33.8, 1.8), (-4.4, 9.6, 1.35, -29.8, 1.3), (9.27, 4.64, 1.35, -31.2, 1.4), (9.15, 12.0, 1.35, -33.0, 1.5))

def dk(receiver_number, potency_k):
    return(math.pow(10.0, ((receiver[receiver_number][3] - potency_k) / (10.0 * receiver[receiver_number][4]))))

def const_factor(receiver_number):
    return(math.pow(receiver[receiver_number][0], 2) + math.pow(receiver[receiver_number][1], 1) + math.pow(receiver[receiver_number][2], 2))

def mmq(receiver_position):
    a = np.matrix([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
    b = np.matrix([[0.0],[0.0],[0.0],[0.0]])
    for i in range(4):
        for j in range(2):
            a[i,j] =  receiver[i + 1][j] - receiver[0][j]
    for i in range(4):
        b[i,0] = math.pow(dk(0, receiver_position[0]), 2) - math.pow(dk(i + 1, receiver_position[i + 1]), 2)
    a = 2 * a
    return (np.linalg.inv(a.transpose() * a) * a.transpose() * b)

read_position = tuple(map(float, input().split()))
resp = mmq(read_position)

''' plot no grafico '''

plot_receiver1 = plt.Circle((1.55,17.63), dk(0, read_position[0]), color = 'r', alpha = .6)
plot_receiver2 = plt.Circle((-4.02,0.0),  dk(1, read_position[1]), color = 'b', alpha = .6)
plot_receiver3 = plt.Circle((-4.4, 9.6),  dk(2, read_position[2]), color = 'm', alpha = .6)
plot_receiver4 = plt.Circle((9.27,4.64),  dk(3, read_position[3]), color = 'y', alpha = .6)
plot_receiver5 = plt.Circle((9.15,12.0),  dk(4, read_position[4]), color = 'k', alpha = .6)
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