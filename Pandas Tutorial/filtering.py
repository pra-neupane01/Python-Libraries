import pandas as pd 

pd.set_option('display.max_columns', None)
df = pd.read_csv("Pandas Tutorial/IPL_Matches_2008_2022.csv")
# print(df.head(5))

finalist = df[df["MatchNumber"] == "Final"]
print(finalist)
thrillingmatch = df[(df["WonBy"] == "Runs") & (df["Margin"] <= 10)]
print(thrillingmatch)