import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([3, 2.5, 2])
y = np.array([1.5, 0.8, 0.5])


# Define the function to fit the data
def func(x, c, d):  # a, b,
    return c * x + d  # a * x**3 + b * x**2 +


# Use curve_fit to approximate the function to the data
popt1, pcov1 = curve_fit(func, x, y)

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 250)

# Calculate the y values for the curve using the fitted function
y_curve = func(x_curve, *popt1)


x_staff = np.linspace(0.5, 2, 10)
y_staff = np.linspace(0, 0, 10)
# Plot the points and the curve
# plt.plot(x, y1, linestyle="--", marker="o", c="blue", label=r"$M_{в}$")
plt.plot(x_staff, y_staff, color="blue", label=r"$M_{ср}$")
plt.plot([2, 2], [0, 0.5], color="blue", linestyle="--", label=r"$M_{ср}$")
plt.scatter([0.5, 1, 1.5], [0, 0, 0], color="blue", linewidth=3)
plt.plot(x_curve, y_curve, color="blue")
plt.scatter(x, y, color="blue", linewidth=3)

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "Зависимость амплитуды генерации от величины\nобратной связи М в жёстком режиме",
    fontsize=14,
    linespacing=1,
)
plt.xlabel(r"обратная связь М", fontsize=14, linespacing=1.5)
plt.ylabel(r"$U_{ген}$, В", fontsize=14, linespacing=1.5)
# plt.legend()

# Show the plot
plt.show()
