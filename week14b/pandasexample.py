import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("table.txt", sep='\t')

plt.plot(df["balance"])
plt.savefig("aaaaa.png")
