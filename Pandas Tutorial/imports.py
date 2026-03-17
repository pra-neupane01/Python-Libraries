import pandas as pd

df = pd.read_csv("Pandas Tutorial/IPL_Matches_2008_2022.csv", index_col="WinningTeam")
print(df.head())

#SELECTION BY COLUMN 
print(df[["City","Team1","Team2","WinningTeam"]].to_string())

#SELECTION BY ROWS
print(df.loc["Mumbai Indians", ["City","Team1","Team2"]])
print(df.iloc[0:20:2,0:4])



winner = input("Enter a winning team")
try:
    print(df.loc[winner])
except KeyError:
    print("Winner Not Found.")    