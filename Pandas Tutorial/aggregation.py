import pandas as pd

df = pd.read_csv("Pandas Tutorial/IPL_Matches_2008_2022.csv")


#whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))

#single column
print(df["Margin"].mean())
print(df["Margin"].sum())
print(df["Margin"].max())
print(df["Margin"].min())
print(df["SuperOver"].count())


# use of group by 
group = df.groupby("TossWinner")
print(group["TossWinner"].count())

