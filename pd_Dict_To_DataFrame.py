

import pandas as pd

dict1 = {"S.No": [1,2],"Name": ["Seeta","Geeta"],"Age": [22,24]}
print(dict1)

# ----------Dictionary To DataFrame Convertion--------------

df_dict=pd.DataFrame(dict1)
print(df_dict)