import matplotlib.pyplot as plt

x_values5000 = list(range(1, 5001))
y_values5000 = [x**3 for x in x_values5000]

plt.scatter(x_values5000, y_values5000, c=y_values5000, cmap=plt.cm.Reds, edgecolors='none', s=40)
plt.title('Cube Numbers', fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.axis([0, 5100, 0, 5100**3])
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()