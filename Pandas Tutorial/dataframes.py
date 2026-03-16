import pandas as pd

data = {
        "Name":["Spongebob","Patrick","Squidward"],
        "Age":[30,35,50]
        }
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
print(df.loc["Employee 1"])
print(df.iloc[0])

#add a new column
df["job"] = ["Cook","N/A","Cashier"]

#add a new row
new_row = pd.DataFrame([{"Name":"Sandy", "Age":28, "job":"Engineer"}], index=["Employee 4"])
df = pd.concat([df, new_row])
print(df)