import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy import interpolate
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([923, 831, 766, 701, 666, 598, 505, 472, 397, 365, 330])
y1 = np.array([0.63, 0.56, 0.50, 0.48, 0.43, 0.40, 0.33, 0.31, 0.26, 0.24, 0.22])
y2 = np.array(
    [
        0.63,
        0.56,
        0.53,
        0.56,
        0.53,
        0.45,
        0.38,
        0.34,
        0.30,
        0.26,
        0.24,
    ]
)


# Define the function to fit the data
def func(x, a, b, c, d):
    return c * x + d  # a * x**3 + b * x**2 +


# Use curve_fit to approximate the function to the data
popt1, pcov1 = curve_fit(func, x, y1)
f = interpolate.interp1d(x, y2, kind="cubic")

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 1000)


# Calculate the y values for the curve using the fitted function
y1_curve = func(x_curve, *popt1)
# y2_curve = func(x_curve, *popt2)
y2_curve = f(x_curve)

# Plot the points and the curve
plt.plot(x, y1, "o", c="blue", label="Теоретические значения")
plt.plot(x, y2, "o", label="Экспериментальные значения")
plt.plot(x_curve, y1_curve, label="Теоретический апроксимирующий полином")
plt.plot(x_curve, y2_curve, label="Экспериментальный интерполирующий полином")

# Add grid, title, axis labels and legend
plt.grid(True)
# plt.title(
#     "Градуировочный график зависимости частоты\n колебательного контура от ёмкости конденсатора",
#     fontsize=14,
#     linespacing=1.5,
# )
plt.xlabel(r"Тока заряда $I_{з}$, мкА", fontsize=14, linespacing=1.5)
plt.ylabel("Частота колебаний динистора c\n" + r"лавинным транзистором, $f_{дин}$, Гц", fontsize=14, linespacing=1.5)
plt.legend()

# Show the plot
plt.show()
