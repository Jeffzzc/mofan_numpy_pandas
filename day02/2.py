import numpy as np
import pandas as pd

dates = pd.date_range('20250101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=list('ABCD'))
print(df)
print(df['A'])
print(df.A)

# select by label: loc
print(df.loc[dates[0]])
print(df.iloc[[1,3,5],1:3])

