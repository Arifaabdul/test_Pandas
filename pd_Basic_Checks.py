

import pandas as pd

df=pd.read_excel(r"C:\\Users\Abdul\\arifa_abdul\\Excel_data.xlsx")
print(df)

# -----Basic Checks-------

print(df.columns)

print(df.shape)

print(df.head())

print(df.head(7))

print(df.tail())

print(df.dtypes)

print(df.info())

print(df.index)


