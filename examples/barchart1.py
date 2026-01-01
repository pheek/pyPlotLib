# main.py
from plotting_lib import create_swiss_coordinate_system, draw_bar_chart,save_system
import matplotlib.pyplot as plt


# 1. System erstellen, das bei 0 startet (z.B. bis x=6, y=5)
# Wir geben -1 als Min an, damit die Achsen nach links/unten noch etwas Platz haben
fig, ax = create_swiss_coordinate_system(0, 6, 0, 5)

# 2. Daten definieren
monate_x = [1, 2, 3, 4, 5]
werte_y  = [2, 4, 3, 5, 1]

# 3. Säulen zeichnen
draw_bar_chart(ax, monate_x, werte_y, label="Verkäufe", color='#e67e22')

ax.legend()

save_system(fig, "barchart1.png")
save_system(fig, "barchart1.eps")

plt.show()


