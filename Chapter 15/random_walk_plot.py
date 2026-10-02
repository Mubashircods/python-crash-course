from random_walk import RendomWalk
import matplotlib.pyplot as plt


# while True:
rw = RendomWalk(50_000)
rw.fill_walk()
color_map = range(rw.num_points)

plt.style.use('classic')
fig, rw_plot = plt.subplots( figsize=(13,6), )
rw_plot.scatter(rw.x_values, rw.y_values, c=color_map,
                cmap=plt.cm.Blues, edgecolors='none', s=1)
rw_plot.set_aspect('equal')

rw_plot.scatter(0, 0, c='green', edgecolors='none', s=100)
rw_plot.scatter(rw.x_values[-1], rw.y_values[-1], c='r',
                edgecolors='none', s=100)
rw_plot.get_xaxis().set_visible(False)
rw_plot.get_yaxis().set_visible(False)
plt.show()

    # keep_running = input("Want to seen more rendom walk? (y/n): ")
    # if keep_running == 'n' or keep_running == 'N':
    #     break

