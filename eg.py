import pandas as pd
import json

# df = pd.read_csv("clean.csv")

# df.to_json("cleanercsv.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

# print(pd.options.display.max_rows)
# pd.options.display.max_rows = 9999

# df = pd.read_csv('data.csv')   

# new_df = df.dropna()  drop empty rows
# df.fillna(130, inplace = True)

# print(new_df.to_string())

# x = df["Calories"].mean()

# df["Calories"].fillna(x, inplace = True)

# x = df["Calories"].median()

# x = df["Calories"].mode()[0]

# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace = True)
# df.loc[7, 'Duration'] = 45
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)

# print(df.duplicated())
# df.drop_duplicates(inplace = True)

# import matplotlib.pyplot as plt

# df = pd.read_csv('clean.csv', low_memory=False)

# diction = df.to_json(   orient = "records", 
#                         date_format = "epoch", 
#                         double_precision = 10, 
#                         force_ascii = True, 
#                         date_unit = "ms", 
#                         default_handler = None
#                     )

# listion = json.loads(diction)

data = {
    1 : "sam",
    2 : "sammy"
}

print(   f'"{data[1]}"'  +  data[2]  )


