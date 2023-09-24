import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
y1 = np.array([1.16, 1.15, 1.13, 1.1, 1.0, 1.0, 1.05, 1.07, 1.0, 0.98, 0.96])
y2 = np.array([0.8, 0.7, 0.5, 0])
y3 = np.array([0, 0.4, 0.6, 0.7, 0.8, 0.84])

# Define the function to fit the data
def func(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e


# Use curve_fit to approximate the function to the data
# popt1, pcov1 = curve_fit(func, x, y1)
# popt2, pcov2 = curve_fit(func, x, y2)
popt1 = interp1d(x, y1, kind="cubic")
popt2 = interp1d(x[:4], y2, kind="cubic")
popt3 = interp1d(x[-6:], y3, kind="cubic")

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 1000)
x_curve2 = np.linspace(x[0], x[3], 1000)
x_curve3 = np.linspace(x[-6], x[-1], 1000)

# Calculate the y values for the curve using the fitted function
# y1_curve = func(x_curve, *popt1)
# y2_curve = func(x_curve, *popt2)
y1_curve = popt1(x_curve)
y2_curve = popt2(x_curve2)
y3_curve = popt3(x_curve3)

# Plot the points and the curve
plt.plot(x, y1, "o", c="blue", label="Экспериментальные значения\nамплитуды для минимума связи")
plt.plot(x[:4], y2, "o", label="Экспериментальные значения амплитуды\nдля максимума связи")
plt.plot(x[-6:], y3, "o")
plt.plot(x_curve, y1_curve, label="Апроксимирующий полином для\nамплитуды минимума связи")
plt.plot(x_curve2, y2_curve, label="Апроксимирующий полином для\nамплитуды максимума связи")
plt.plot(x_curve3, y3_curve)

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "График зависимости амплитуды колебательного\n контура от ёмкости конденсатора",
    fontsize=14,
    linespacing=1.5,
)
plt.xlabel(r"Ёмкость $С_1$, нФ", fontsize=14, linespacing=1.5)
plt.ylabel(r"Амплитуда колебательного контура $C_1 L_1$, В", fontsize=14, linespacing=1.5)
plt.legend()

# Show the plot
plt.show()
