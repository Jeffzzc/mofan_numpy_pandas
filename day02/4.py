
from __future__ import print_function
import pandas as pd

# read from
data = pd.read_csv('student.csv')
print(data)

# save to
data.to_pickle('student.pickle')