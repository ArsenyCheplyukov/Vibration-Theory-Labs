import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x1 = np.array([1007, 985, 951, 909, 866, 822, 783, 735, 695, 660, 638])
x2 = np.array([1043, 1018, 985, 941, 901, 858, 814, 771, 733, 698, 680])
# y1 = np.array([1.15, 1.1, 1.07, 1.04, 1.0, 1.0, 1.05, 1.08, 1.1, 1.12, 1.15])
# y2 = np.array([0.95, 0.9, 0.85, 0.74, 0.5, 0.7, 0.84, 0.9, 1, 1.05, 1.06])

# y1 = np.array([1.16, 1.15, 1.13, 1.1, 1.0, 1.0, 1.05, 1.07, 1.0, 0.98, 0.96])
# y2 = np.array([0.8, 0.7, 0.6, 0, 0, 0, 0.4, 0.6, 0.7, 0.8, 0.82])

# y1 = np.array([1009, 989, 952, 907, 868, 818, 777, 732, 696, 658, 656])
# y2 = np.array([1075, 1075, 1023, 989, 0, 0, 737, 701, 668, 639, 620])

y1 = np.array([1010, 990, 949, 911, 970, 818, 777, 735, 693, 661, 636])
y2 = np.array([1079, 1060, 1028, 999, 970, 753, 728, 698, 666, 637, 619])

# Define the function to fit the data
# def func(x, a, b, c, d):
#     return a * x**3 + b * x**2 + c * x + d


# Use curve_fit to approximate the function to the data
# popt1, pcov1 = curve_fit(func, x, y1)
# popt2, pcov2 = curve_fit(func, x, y2)

# Define the x values for the curve
# x_curve = np.linspace(np.min(x), np.max(x), 1000)

# Calculate the y values for the curve using the fitted function
# y1_curve = func(x_curve, *popt1)
# y2_curve = func(x_curve, *popt2)

# Plot the points and the curve
plt.plot(
    x1,
    y1,
    linestyle="--",
    marker="o",
    c="blue",
    label="Экспериментальные значения частоты\n генерации для минимума связи",
)
plt.plot(
    x2,
    y2,
    linestyle="--",
    marker="o",
    c="red",
    label="Экспериментальные значения частоты\n генерации для максимума связи",
)
# plt.plot(x_curve, y1_curve, label="Апроксимирующий полином частоты для минимума связи")
# plt.plot(x_curve, y2_curve, label="Апроксимирующий полином частоты для максимума связи")

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "График зависимости частоты генерации\n колебательного контура от собственной частоты",
    fontsize=14,
    linespacing=1.5,
)
plt.ylabel(r"Частота генерированных колебаний контура ${\nu}_{ген}$, кГц", fontsize=14, linespacing=1.5)
plt.xlabel(r"Частота собственный колебаний контура ${\nu}_{соб}$, кГц", fontsize=14, linespacing=1.5)
plt.legend()

# Show the plot
plt.show()
