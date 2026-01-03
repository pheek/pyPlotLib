#!/usr/bin/python3
from bms_graph_lib import create_swiss_coordinate_system, draw_bar_chart, set_custom_labels,save_system
import matplotlib.pyplot as plt

# 1. System erstellen (x von 0 bis 5, y von 0 bis 6)
fig, ax = create_swiss_coordinate_system(0, 5, 0, 6)

# 2. Daten definierensave_system(fig, "barchart1.png")

pos_x = [1, 2, 3, 4, 5]
groessen = ["XS", "S", "M", "L", "XL"]
anzahl = [1, 3, 5, 4, 2]

# 3. Säulen zeichnen
draw_bar_chart(ax, pos_x, anzahl, color='#8e44ad') # Ein schönes Violett

# 4. Namen statt Zahlen an die x-Achse schreiben
set_custom_labels(ax, pos_x, groessen)

#optional:
#evtl schief stellen
ax.set_xticklabels(groessen, fontweight='bold', ha='right')


ax.legend(["Verkäufe"])

save_system(fig, "barchart2.png")
plt.show()
