import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy import interpolate
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([0, -0.5, -1.0, -1.5, -2.0, -2.5, -3.0, -3.33])
y = np.array([90.0, 86.6, 83.0, 80.4, 79.7, 77.8, 75.3, 71.9])

# Define the function to fit the data
# def func(x, c, d): # a, b,
# return c * x + d # a * x**3 + b * x**2 +


# Use curve_fit to approximate the function to the data
# popt, pcov = curve_fit(func, x, y)
f = interpolate.interp1d(x, y, kind="cubic")

# Define the x values for the curve

x_curve = np.linspace(np.min(x), np.max(x), 1000)
y1_curve = f(x_curve)

# Calculate the y values for the curve using the fitted function
# y1_curve = func(x_curve, *popt)

# Plot the points and the curve
plt.plot(x, y, "o", c="blue", label="Экспериментальные значения")
plt.plot(x_curve, y1_curve, label="Апроксимирующий полином")

# Add grid, title, axis labels and legend
plt.grid(True)
# plt.title(
#     "",
#     fontsize=14,
#     linespacing=1.5,
# )
plt.xlabel("Напряжение на диоде U, В", fontsize=14, linespacing=1.5)
plt.ylabel("Ёмкость диода С, пФ", fontsize=14, linespacing=1.5)
# plt.legend()

# Show the plot
plt.show()
