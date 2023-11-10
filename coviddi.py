import pandas as pd

data = pd.read_csv('TEST.csv',
                   index_col='data',
                   sep=',',
                   parse_dates=True,
                   usecols=[0, 3, 10])

print(data.head(n=10))
