import numpy as np 
import math 

receiver = ((1.55, 17.63, 2.0, -26.0, 2.1), (-4.02, 0.0, 1.35, -33.8, 1.8), (-4.4, 9.6, 1.35, -29.8, 1.3), (9.27, 4.64, 1.35, -31.2, 1.4), (9.15, 12.0, 1.35, -33.0, 1.5))

def dk(receiver_number, potency_k):
    return(math.pow(10.0, ((receiver[receiver_number][3] - potency_k) / (10.0 * receiver[receiver_number][4]))))

def const_factor(receiver_number):
    return(math.pow(receiver[receiver_number][0], 2) + math.pow(receiver[receiver_number][1], 1) + math.pow(receiver[receiver_number][2], 2))

def mmq(receiver_position):
    a = np.matrix([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    b = np.matrix([[0.0],[0.0],[0.0],[0.0]])
    for i in range(4):
        for j in range(3):
            a[i,j] =  receiver[i + 1][j] - receiver[0][j]
    for i in range(4):
        b[i,0] = math.pow(dk(0, receiver_position[0]), 2) - math.pow(dk(i + 1, receiver_position[i + 1]), 2)
    a2 = 2.0 * a
    inv = (a.transpose() * a2)
    print(np.linalg.inv(inv)*a.transpose()*b)

read_position = tuple(map(float, input().split()))
print(mmq(read_position))