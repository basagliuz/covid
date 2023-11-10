import pandas as pd

cov = pd.read_csv('TEST.csv', index_col = 0, parse_dates = True)
cov.head()