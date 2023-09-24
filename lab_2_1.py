import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
from scipy import interpolate

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]


data = pd.read_excel("lab_2_1.xlsx", header=None)
x = data.iloc[1:, 0].to_numpy()
y = data.iloc[1:, 3].to_numpy()
print(x)

z = interpolate.interp1d(x, y, kind="cubic")
x_curve = np.linspace(np.min(x), np.max(x), 250)
y_curve = z(x_curve)

plt.plot(x_curve, y_curve, color="red")
plt.scatter(x, y, color="red", linewidth=3)

# print(data)

# Add grid, title, axis labels and legend
plt.grid(True)
plt.title(
    "Зависимость ширины области захвата\n от амплитуды внешнего сигнала",
    fontsize=14,
    linespacing=1,
)
plt.xlabel(r"Амплитуда внешнего сигнала, $10^{-4}$В", fontsize=14, linespacing=1.5)
plt.ylabel(r"Ширина области захвата $\Delta$f, МГц", fontsize=14, linespacing=1.5)
plt.show()
