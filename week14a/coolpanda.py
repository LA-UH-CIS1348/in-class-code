import pandas as pd

df = pd.read_csv("tsv.txt", sep='\t')
print(df[['age','height']])