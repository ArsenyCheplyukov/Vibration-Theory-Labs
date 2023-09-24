import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
from scipy import interpolate

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]


data = pd.read_excel("lab_2_3.xlsx", header=None)
x1 = data.iloc[1:, 0].to_numpy()[:5]
y1 = data.iloc[1:, 1].to_numpy()[:5]

# x2 = data.iloc[1:, 2].to_numpy()
# y2 = data.iloc[1:, 3].to_numpy()

z1 = interpolate.interp1d(x1, y1, kind="cubic")
x_curve_1 = np.linspace(np.min(x1), np.max(x1), 250)
y_curve_1 = z1(x_curve_1)

# z2 = interpolate.interp1d(x2, y2, kind="cubic")
# x_curve_2 = np.linspace(np.min(x2), np.max(x2), 250)
# y_curve_2 = z2(x_curve_2)

plt.plot(x_curve_1, y_curve_1, color="red")
plt.scatter(x1, y1, color="red", linewidth=3)

# plt.plot(x_curve_2, y_curve_2, color="blue")
# plt.scatter(x2, y2, color="blue", linewidth=3)

# print(data)

# Add grid, title, axis labels and legend
plt.grid(True)
# plt.title(
#     "Зависимость амплитуды колебаний в области захватывания от\n частоты при большом и малом внешнем воздействии",
#     fontsize=14,
#     linespacing=1,
# )
plt.xlabel(
    r"Амплитуда колебаний в области захватывания, $10^{-4}$В",
    fontsize=14,
    linespacing=1.5,
)
plt.ylabel(
    r"Частота при большом внешнем воздействии $\Delta$f, МГц",
    fontsize=14,
    linespacing=1.5,
)
plt.show()
