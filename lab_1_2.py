import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([3, 2.5, 2, 1.5])
y = np.array([1.1, 0.9, 0.7, 0.3])


# Define the function to fit the data
def func(x, a, b, c, d):
    return b * x**2 + c * x + d  # a * x**3 +


# Use curve_fit to approximate the function to the data
popt1, pcov1 = curve_fit(func, x, y)

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 250)

# Calculate the y values for the curve using the fitted function
y_curve = func(x_curve, *popt1)

staff_x = np.linspace(0.5, 1.5, 10)
staff_y = 0.015 * staff_x + 0.005
# Plot the points and the curve
plt.plot(staff_x, staff_y, c="blue", label=r"$M_{в}$")
plt.plot(
    [1.5, 1.5, 1.5, 1.5],
    [0.0275, 0.1, 0.2, 0.3],
    linestyle="--",
    c="blue",
    label=r"$M_{в}$",
)
plt.scatter([0.5, 1], [0, 0], color="blue", linewidth=3)
# plt.plot(x, y2, linestyle="--", marker="o", label=r"$M_{ср}$")
plt.plot(x_curve, y_curve, color="blue")
plt.scatter(x, y, color="blue", linewidth=3)

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "Зависимость амплитуды генерации от величины\nобратной связи М в мягком режиме",
    fontsize=14,
    linespacing=1,
)
plt.xlabel(r"обратная связь М", fontsize=14, linespacing=1.5)
plt.ylabel(r"$U_{ген}$, В", fontsize=14, linespacing=1.5)
# plt.legend()

# Show the plot
plt.show()
