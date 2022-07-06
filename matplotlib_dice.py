# Using the library Matplotlib to make a die-rolling visualisation
# TeenAsher

import matplotlib.pyplot as plt
from die import Die

die = Die()

results = []
for num_roll in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = range(1, die.num_sides+1)
y_values = frequencies

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.viridis, linewidth=3)

ax.set_title('Results of rolling one D6 1000 times', fontsize=24)
ax.set_xlabel('Result', fontsize=14)
ax.set_ylabel('Frequency of result', fontsize=14)

plt.show()
