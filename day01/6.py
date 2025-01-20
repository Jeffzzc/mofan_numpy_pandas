import numpy as np

A = np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.clip(A,5,9)) # 门限函数，大于9的全取为9，小于5的全取为5
print(np.mean(A, axis=0))
print(np.mean(A, axis=1))