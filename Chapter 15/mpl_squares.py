import matplotlib.pyplot as plt


input_value = [1, 2, 3, 4, 5]
square = [1,4,9,16,25,]

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(input_value, square, linewidth=2)

ax.set_title("Square numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of values.", fontsize=14)

ax.tick_params(labelsize=14)
plt.show()




