import pandas as pd 

data = [100,101,200,100,99,104]
series = pd.Series(data, index=["a","b","c","d","e","f"])
print(series.loc["a"])
print(series.iloc[1])
series.loc["a"] = 98
print(series[series > 100])

milk_per_day = {"Day 1": 10, "Day 2": 11, "Day 3": 13, "Day 4": 14, "Day 5": 13, "Day 6": 14 }
series = pd.Series(milk_per_day)
print(series)

