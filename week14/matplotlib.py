import matplotlib.pyplot as plt

#x = [1,2,3,4,5,6,6,8,9,2,2,4,3,2,1]
#plt.plot(x)
#plt.savefig("lineplot.png")

"""
x = [1,2,3,4,4,3,2,1,5,67,43,2,2,56,43,2,2,120,120,120,210,122,122]
y = [14,12,63,14,4,73,72,31,25,6,4,21,12,6,3,12,12,120,120,120,120,125,125]
plt.scatter(x,y)
plt.savefig("scatterplot.png")
"""

lines = open("data.txt", "r").readlines()
x=[]
y=[]
for l in lines:
    parts = l.split()
    x.append(float(parts[0]))
    y.append(float(parts[1]))

#plt.scatter(x,y)
#plt.savefig("scatterplot.png")

#plt.hist(x, bins=100)
#plt.savefig("histogram.png")

categories = ["XBOX","PS5","SWITCH"]
values =  [400,200,700]
plt.bar(categories, values)
plt.savefig("barplot.png")