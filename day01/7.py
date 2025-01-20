import numpy as np

A = np.arange(3,15).reshape(3,4)
print(A)
print(A[2][1])
print(A[1,1:2])

for row in A:
    print(row)
print("=============")
for column in A.T:
    print(column)
print("=============")
for item in A.flat:
    print(item)
print(A.flatten())      # 返回转换之后的array