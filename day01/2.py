import numpy as np

a = np.array([2,23,4],dtype=np.float64)
print(a.dtype)
print("===================")
b = np.array([[2,23,4],
              [2,23,4]])
print(b)
b = np.zeros((3,4))
print(b)
b = np.ones((3,4),dtype=np.float64)
print(b)
b = np.empty((3,4))
print(b)
print("===================")
c = np.arange(12).reshape(3,4)
print(c)
c = np.linspace(1,10,6).reshape(2,3)
print(c)