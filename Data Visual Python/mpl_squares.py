## tutorial from Python textbook

import matplotlib.pyplot as plt
plt.style.available

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

# remove line of code to get corrected graph - ax.plot(squares, linewidth=3)

# set chart title/label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()