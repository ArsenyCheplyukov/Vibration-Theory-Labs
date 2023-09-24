import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]

# Define the x and y arrays
x = np.array(
    [
        -4.38,
        -4.54,
        -4.75,
        -4.97,
        -5.89,
        -6.47,
        -7.75,
        -3.6,
        -3.0,
        -2.45,
        -1.94,
        -0.93,
        -0.16,
        0,
    ]
)
y = np.array([17, 16, 16, 16, 16, 16, 15, 17, 17.8, 18, 18, 18, 18, 18])


# Define the function to fit the data
def func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d


# Use curve_fit to approximate the function to the data
popt1, pcov1 = curve_fit(func, x, y)

# Define the x values for the curve
x_curve = np.linspace(np.min(x), np.max(x), 250)

# Calculate the y values for the curve using the fitted function
y_curve = func(x_curve, *popt1)

# Plot the points and the curve
# plt.plot(x, y, linestyle="--", marker="o", c="blue", label=r"$M_{в}$")
# plt.plot(x, y2, linestyle="--", marker="o", label=r"$M_{ср}$")
plt.plot(x_curve, y_curve, color="blue")
plt.scatter(x, y, color="blue", linewidth=3)

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "Зависимость тока стока от напряжения на затворе",
    fontsize=14,
    linespacing=1,
)
plt.xlabel("U, В", fontsize=14, linespacing=1.5)
plt.ylabel("I, мкА", fontsize=14, linespacing=1.5)
# plt.legend()

# Show the plot
plt.show()
