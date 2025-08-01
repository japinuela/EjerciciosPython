import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints, marker='o', color='green', linestyle='dashed', linewidth=2, markersize=12)

# #plt.plot(xpoints, ypoints, marker='o')
# #Default x-axis
# #ypoints = np.array([3, 8, 1, 10, 5, 7])
# #plt.plot(ypoints)
# plt.show()

#Version con Dataframes
# Datos
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# 🔹 1. Mostrar la tabla con tools
df = pd.DataFrame({"X": xpoints, "Y": ypoints})
print(df)

# 🔹 2. Graficar con matplotlib
plt.plot(xpoints, ypoints, marker='o', color='green',
         linestyle='dashed', linewidth=2, markersize=12)
plt.title("Ejemplo de línea con Matplotlib")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid()
plt.show()

