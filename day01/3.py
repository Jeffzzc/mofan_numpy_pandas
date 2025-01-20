import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)

print(a,b)
c=a+b
print(c)
d=a**2
print(d)
e=10*np.sin(a)
print(e)
print(b<3)
print(b==3)
print("=====================")
f = np.array([[1,2],
              [3,4]])
g = np.arange(4).reshape(2,2)
print(f)
print(g)
print("=====================")
h = f*g              # 逐个×
print(h)
i = np.dot(f,g)      # 点乘
print(i)
i_2 = f.dot(g)
print(i_2)