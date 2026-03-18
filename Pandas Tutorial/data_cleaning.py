import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv("Pandas Tutorial/IPL_Matches_2008_2022.csv")

#1. drop irrelevant columns 
df = df.drop(columns=["method"])
print(df)