import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
print("# Publications \n\n")
for index, row in df.iterrows():
    print(f"* [{row['Title']}]({row['PID']}) by {row['Authors']}")
