import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]
y2 = [1,4,9,16,25]

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(x,y)
ax2 = fig.add_subplot(2,1,2)
ax2.plot(x,y2)

plt.show()