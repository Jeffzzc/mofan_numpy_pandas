import numpy as np
import pandas as pd

s = pd.Series([1,3,6,np.nan,44,1])
print(s)
dates = pd.date_range('20250120',periods=6)
print(dates)
print("==========================================================================")
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
print("==========================================================================")
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)