import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
y1 = np.array([1009, 989, 952, 907, 868, 818, 777, 732, 696, 658, 656])
y2 = np.array([1075, 1075, 1023, 989, 0, 0, 737, 701, 668, 639, 620])

# Define the function to fit the data
def func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d  


# Use curve_fit to approximate the function to the data
# popt1, pcov1 = curve_fit(func, x, y1)
# popt2, pcov2 = curve_fit(func, x, y2)

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 1000)

# Calculate the y values for the curve using the fitted function
# y1_curve = func(x_curve, *popt1)
# y2_curve = func(x_curve, *popt2)

# Plot the points and the curve
plt.plot(x, y1, linestyle="--", marker="o", c="blue", label="Экспериментальные значения\nчастоты для минимума связи")
plt.plot(x, y2, linestyle="--", marker="o", label="Экспериментальные значения частоты\nдля максимума связи")
# plt.plot(x_curve, y1_curve, label="Апроксимирующий полином частоты для минимума связи")
# plt.plot(x_curve, y2_curve, label="Апроксимирующий полином частоты для максимума связи")

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "График зависимости частоты\n колебательного контура от ёмкости конденсатора",
    fontsize=14,
    linespacing=1.5,
)
plt.xlabel(r"Ёмкость $С_1$, нФ", fontsize=14, linespacing=1.5)
plt.ylabel(r"Частота колебательного контура $C_1 L_1$, кГц", fontsize=14, linespacing=1.5)
plt.legend()

# Show the plot
plt.show()
