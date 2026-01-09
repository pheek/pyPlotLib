#!/usr/bin/python3
from bms_graph_lib import bmsw_coordinate_system, draw_bar_chart, set_custom_labels,save_system
import matplotlib.pyplot as plt

# 1. System erstellen (x von 0 bis 5, y von 0 bis 6)
fig, ax = bmsw_coordinate_system(0, 6, 0, 6)

# 2. Daten definierensave_system(fig, "barchart1.png")

pos_x = [1, 2, 3, 4, 5, 6]
groessen = ["extra small", "small", "medium", "large", "extra large", "bombastic"]
anzahl = [1, 3, 5, 4, 2, 8]

# 3. Säulen zeichnen
draw_bar_chart(ax, pos_x, anzahl, color='#8e2288') # Ein schönes Violett

# 4. Namen statt Zahlen an die x-Achse schreiben
set_custom_labels(ax, pos_x, groessen)

#optional:
#evtl schief stellen
ax.set_xticklabels(groessen, fontweight='bold', rotation=60, ha='right')

ax.legend(["Verkäufe Autos"])

save_system(fig, "barchart3.png")
plt.show()
