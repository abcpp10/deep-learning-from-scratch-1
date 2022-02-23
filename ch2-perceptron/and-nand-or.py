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
print(andgate(1,0))
print(andgate(0,1))
print(andgate(1,1))
#0001


def nandgate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

print(nandgate(0,0))
print(nandgate(1,0))
print(nandgate(0,1))
print(nandgate(1,1))
#1110


def orgate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    else:
        return 1

print(orgate(0,0))
print(orgate(1,0))
print(orgate(0,1))
print(orgate(1,1))
#0111
