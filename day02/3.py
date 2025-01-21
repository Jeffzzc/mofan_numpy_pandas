import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=list('ABCD'))
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df)
print(df.dropna(axis=0, how='any'))
print("=====================================")
print(df.dropna(axis=0, how='all'))
print("=====================================")
print(df.fillna(value=0))
print("=====================================")
print(df.isnull())
print("=====================================")
print(np.any(df.isnull()==True))