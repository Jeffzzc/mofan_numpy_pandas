import numpy as np

a = np.random.random((2,4)) # 从0-1
print(a)
print(np.sum(a, axis=1))
print(np.min(a, axis=0))
print(np.max(a, axis=1))