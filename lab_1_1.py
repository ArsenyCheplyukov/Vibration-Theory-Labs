import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([-4, -3, -2.7, -2.25, -1.6, -1.2, -0.74])
y1 = np.array([1.75, 2, 2.1, 2.4, 2.5, 2.75, 3])
y2 = np.array([1.75, 1.75, 1.75, 1.8, 1.8, 1.9, 1.95])


# Define the function to fit the data
def func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d


# Use curve_fit to approximate the function to the data
popt1, pcov1 = curve_fit(func, x, y1)
popt2, pcov2 = curve_fit(func, x, y2)

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 250)

# Calculate the y values for the curve using the fitted function
y1_curve = func(x_curve, *popt1)
y2_curve = func(x_curve, *popt2)

# Plot the points and the curve
# plt.plot(x, y1, linestyle="--", marker="o", c="blue", label=r"$M_{в}$")
# plt.plot(x, y2, linestyle="--", marker="o", label=r"$M_{ср}$")
plt.plot(x_curve, y1_curve, color="blue", label=r"$M_{в}$")
plt.plot(x_curve, y2_curve, color="red", label=r"$M_{ср}$")
plt.scatter(x, y1, color="blue", linewidth=3)
plt.scatter(x, y2, color="red", linewidth=3)

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    r"Зависимость $М_{ср}$ и $М_{возб}$ от величины отрицательного"
    + "\nнапряжения смещения на затворе транзистора ПТ1",
    fontsize=14,
    linespacing=1,
)
plt.xlabel(r"Отрицательное напряжение смещения, В", fontsize=14, linespacing=1.5)
plt.ylabel(r"$М_{ср}, M_{возб}$", fontsize=14, linespacing=1.5)
plt.legend()

# Show the plot
plt.show()
