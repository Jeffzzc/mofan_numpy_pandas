import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])
C = np.vstack((A,B))  # vertical合并
D = np.hstack((A,B))  # horizontal合并
print(C)
print(D)