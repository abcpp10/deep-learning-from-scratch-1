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

def nandgate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def orgate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def xorgate(x1, x2):
    s1 = nandgate(x1, x2)
    s2 = orgate(x1, x2)
    y = andgate(s1, s2)
    return y

print(xorgate(0,0))
print(xorgate(1,0))
print(xorgate(0,1))
print(xorgate(1,1))
#0110