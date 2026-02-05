import pandas as pd
#import numpy as np
import sys

month = int(sys.argv[1])

df = pd.DataFrame({'A': [1, 2], 'B': [2, 3]})

print(f'Hello pipeline, month is {month}')

print(df.head())
df.to_parquet(f"output_{month}.parquet")