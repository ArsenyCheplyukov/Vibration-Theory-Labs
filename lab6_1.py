import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy import interpolate
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array(
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.625, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
)
y = np.array(
    [
        0.14,
        0.61,
        0.60,
        2.00,
        0.46,
        1.00,
        0.52,
        0.58,
        0.58,
        0.96,
        0.39,
        0.88,
        0.34,
        0.56,
        0.53,
        0.46,
    ]
)

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
plt.ylabel("Напряжение на выходе линии задержки U, В", fontsize=14, linespacing=1.5)
plt.xlabel("Частота внешнего сигнала f, МГц", fontsize=14, linespacing=1.5)
# plt.legend()

# Show the plot
plt.show()
