import pandas as pd

df = pd.read_csv("people.txt", sep='\t')
print(df[["balance","name"]])


