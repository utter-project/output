import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
print("# Participation in Events \n\n")
for group_name, group_df in df.groupby("Type"):
  print(f"## {group_name}")
  for index, row in group_df.iterrows():
      print(f"* To _{row['Audience']}_ in _{int(row['Year'])}_: [{row['Description']}]({row['Outcome']})")
  print("\n")
