#!/usr/bin/python3
from bms_graph_lib import bmsw_coordinate_system, draw_histogram,save_system
import matplotlib.pyplot as plt

# 1. System erstellen (z.B. von 0 bis 10 auf beiden Achsen)
fig, ax = bmsw_coordinate_system(0, 31, 0, 11)

# 2. Beispieldaten (Rohdaten)
# Diese Daten werden vom Histogramm automatisch gezählt
messwerte = [5.5, 5.8, 8.2, 11.6, 11.6, 11.6, 15.6, 8.7, 21.8, 25.3]

# 3. Histogramm einzeichnen
# Start bei 0, jede Säule ist 2 Einheiten breit (0-2, 2-4, 4-6, ...)
draw_histogram(ax, messwerte, bin_width=5, start_value=0, label="Häufigkeit", color='#2ecc71')

ax.legend()

# save (optional) and show
#save_system(fig, "histogramm2.png")
plt.show()
