import pandas as pd

df=pd.read_excel(r"C:\\Users\Abdul\\arifa_abdul\\Excel_data.xlsx")

df1=pd.read_csv(r"C:\\Users\Abdul\\OneDrive\Documents\\STUDENT_DETAILES.csv")

# ---------Concatination or Appending---------------
    
df_new=pd.concat([df,df1],axis=0,ignore_index=True)
print(df_new)

df_new1=pd.concat([df,df1],axis=1,ignore_index=True)
print(df_new1)