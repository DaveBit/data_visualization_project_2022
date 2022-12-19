import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.scatter(x_values, y_values, edgecolors='none', s=40)

plt.title('Cube Numbers', fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()