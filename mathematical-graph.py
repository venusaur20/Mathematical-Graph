import matplotlib.pyplot as plt, numpy as np, math


x_start = 1 #int(input("Start of x-axis: "))
x_finish = 100 #int(input("End of x-axis: "))
accuracy = 0.05 #int(input("Update Interval: "))
x_axis = np.arange(x_start, x_finish, accuracy)

y_axis = 10**(x_axis)

plt.plot(x_axis, y_axis, 'r--')
plt.show()