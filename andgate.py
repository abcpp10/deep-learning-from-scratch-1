import numpy as np

def andgate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    else:
        return 1


print(andgate(0,0))
#0

print(andgate(0,1))
#0

print(andgate(1,1))
#1