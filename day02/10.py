# handle overlapping
import pandas as pd

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')
print(res)

# join function in pandas is similar with merge. If know merge, you will understand join