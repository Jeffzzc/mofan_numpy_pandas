from __future__ import print_function
import pandas as pd
import numpy as np

# concatenating
# ignore index
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# join, ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
print(df1)
print(df2)
res = pd.concat([df1, df2], axis=0, join='outer')
print(res)
res = pd.concat([df1, df2], axis=1, join='inner')
print(res)


print("==================================")

# append
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
res = df1._append(df2, ignore_index=True)
res = df1._append([df2, df3])

s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
res = df1._append(s1, ignore_index=True)

print(res)