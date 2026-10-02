import matplotlib.pyplot as plt


# Solution 15.1
values = [1, 2, 3, 4, 5]
cube = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.scatter(values, cube, c='r', s=40)
# Set the labels
ax.set_title("Cubes", fontsize=20)
ax.set_xlabel("Values", fontsize=12)
ax.set_ylabel("Cubes of values", fontsize=12)
# Adjust tick size and color
ax.tick_params(labelsize=10, color='r')

# Display the plot
plt.show()


# Draw second plot
values = range(1, 5001)
Cubes = [x**3 for x in values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(values, Cubes, c=Cubes, cmap=plt.cm.Reds, s=20)
# set labels and title
ax.set_title("Cubes", fontsize=18)
ax.set_xlabel("Values", fontsize=12)
ax.set_ylabel("Cubes of Values")
# Adjust tick styles
ax.tick_params(labelsize=8, color=(0.9, 0, 0))
ax.ticklabel_format(style='plain')
# ax.axis([0, 5100, 0, 1_22_000_000_000])

# Display plot
plt.show()




# Solution 15.2 is solved in 15.1




# Solution 15.3
from random_walk import RendomWalk

rw = RendomWalk()
rw.fill_walk()
plt.style.use("classic")
fig, rw_plot = plt.subplots()
rw_plot.plot(rw.x_values, rw.y_values, linewidth=1, c='g')
rw_plot.scatter(0, 0, c='green', s=100, edgecolors='none')
rw_plot.scatter(rw.x_values[-1], rw.y_values[-1],
                c='r', s=100, edgecolors='none')

rw_plot.get_xaxis().set_visible(False)
rw_plot.get_yaxis().set_visible(False)
plt.show()




# Solution 15.4 and 15.5
# This problem ask to modify the class rendom walk.
# For do so let's go to module randomwalk ad modify it and then solving the problem.
rws = RendomWalk()
rws.fill_walk()
point_values = range(rws.num_points)
plt.style.use('classic')
fig, rw_s = plt.subplots()
rw_s.scatter(rws.x_values, rws.y_values, c=point_values,
                edgecolors='none', cmap=plt.cm.Reds, s=4)
rw_s.scatter(0, 0, c='green', s=100, edgecolors='none')
rw_s.scatter(rws.x_values[-1], rws.y_values[-1],
                c='r', s=100, edgecolors='none')
rw_s.get_xaxis().set_visible(False)
rw_s.get_yaxis().set_visible(False)
plt.show()





