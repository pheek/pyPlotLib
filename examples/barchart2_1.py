#!/usr/bin/python3
from bms_graph_lib import bmsw_coordinate_system, draw_bar_chart, set_custom_labels,save_system
import matplotlib.pyplot as plt

# 1. System erstellen 
fig, ax = bmsw_coordinate_system(0, 6, 0, 6)

# 2. Daten definieren
pos_x = [1, 2, 3, 4, 5]
groessen = ["XS", "S", "M", "L", "XL"]
anzahl = [1, 3, 5, 4, 2]

# 3. Säulen zeichnen
draw_bar_chart(ax, pos_x, anzahl, color='#8e44ad') # Ein schönes Violett

# 4. Namen statt Zahlen an die x-Achse schreiben
set_custom_labels(ax, pos_x, groessen)

# 5. Labels beschriften
ax.set_xticklabels(groessen, fontweight='bold', ha='right')

# 6. Legende zeichnen
ax.legend(["Verkäufe"])

## save (optional) and show
#save_system(fig, "barchart2.png")
plt.show()
