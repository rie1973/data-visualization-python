## tutorial from Python textbook

import matplotlib.pyplot as plt

# set values for mutliple points
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

#set values with 1000 points
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()

# used to plot single point - ax.scatter(2, 4, s=200), where "s" equal size of point
# used to plot multple points ax.scatter(x_values, y_values, s=100)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#set chart title/label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set range for each axis
ax.axis([0, 1100, 0, 1100000])

# set size of tick labels for multiple points- ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
