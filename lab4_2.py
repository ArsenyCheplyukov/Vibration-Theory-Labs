import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy import interpolate
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([2.0, 2.1, 2.2, 2.3, 2.35, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0])
y = np.array(
    [1.00, 1.20, 1.80, 2.10, 2.30, 2.50, 2.40, 2.20, 1.20, 0.90, 0.55, 0.38, 0.24]
)

# Define the function to fit the data
# def func(x, c, d): # a, b,
#     return c * x + d # a * x**3 + b * x**2 +


# Use curve_fit to approximate the function to the data
# popt, pcov = curve_fit(func, x, y)
# f = interpolate.interp1d(x, y, kind="cubic")

# Define the x values for the curve

# x_curve = np.linspace(np.min(x), np.max(x), 1000)
# y1_curve = f(x_curve)

# Calculate the y values for the curve using the fitted function
# y1_curve = func(x_curve, *popt)

# Plot the points and the curve
plt.plot(x, y, "o", c="blue", label="Экспериментальные значения")
# plt.plot(x_curve, y1_curve, label="Апроксимирующий полином")
plt.plot(x, y, c="blue", label="Экспериментальные значения")

# Add grid, title, axis labels and legend
plt.grid(True)
# plt.title(
#     "",
#     fontsize=14,
#     linespacing=1.5,
# )
plt.xlabel("Частота внешнего сигнала f, МГц", fontsize=14, linespacing=1.5)
plt.ylabel("Амплитуда колебаний на выходе системы U, В", fontsize=14, linespacing=1.5)
# plt.legend()

# Show the plot
plt.show()
