import sys
print(sys.executable)
import pandas as pd
import os

print("test")
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../../data/HOPE_paper2_demographics.xlsx')
csv_filename = os.path.join(dirname, '../../data/HOPE_paper2_demographics.csv')

df = pd.DataFrame(pd.read_excel(filename))
print(df.columns)
print(df.head())
df.to_csv(csv_filename)
