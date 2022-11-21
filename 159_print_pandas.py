import seaborn as sb
import pandas as pd

df = sb.load_dataset('titanic')

print(df)

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', 5000)

print(df)# or 199