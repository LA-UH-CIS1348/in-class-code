import matplotlib.pyplot as plt

#LINEPLOT
y = [1,2,3,1,2,3,1,2,3,7,8,9]
#plt.plot(y)
#plt.show()
#plt.savefig("line.png")

#SCATTERPLOT
"""
x = [20,60,12,16,4.2,200]
y = [3,1.2,0.8,1.4,52,9.2]
plt.scatter(x,y)
plt.savefig("scatter.png")
"""

data = [192,50,293,120,90,45,67,92,52,200,205,78,35,120,138,72,121,345,92,61,201]
plt.hist(data, bins=20)
plt.savefig("hist.png")