'''import pandas as pd
import numpy as np

df = pd.read_csv("Housing.csv")

df = df.select_dtypes(include=np.number)

max_abs = np.max(np.abs(df), axis=0)
scaled_df = df/max_abs
scaled_df.head()
#df.head()'''

from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id = 53)
