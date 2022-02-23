import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

case = a>1
print(case)

print(a[case])
#[2 3 4 5 6]
