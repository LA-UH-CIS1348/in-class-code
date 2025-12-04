import matplotlib.pyplot as plt
import random

l = open("data.txt","r").readlines()
x = []
for line in l:
    x.append(float(line.strip()))
"""
plt.plot(x)
plt.title("Aaaaaaaaaaaaaaaaaaaa")
plt.xlabel("time")
plt.ylabel("money")
plt.savefig("lineplot.png")
"""
#plt.hist(x)
#plt.savefig("histogram.png")

y = []
for a in x:
    y.append(random.random())

#plt.scatter(x,y)
#plt.savefig("scatter.png")

value = [200,400,100]
category = ["AAA","BBB","CCC"]
plt.bar(category,value)
plt.savefig("bar.png")