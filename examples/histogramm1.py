#!/usr/bin/python3
from bms_graph_lib import create_swiss_coordinate_system, draw_histogram, save_system
import matplotlib.pyplot as plt

# 1. System erstellen (z.B. von 0 bis 10 auf beiden Achsen)
fig, ax = create_swiss_coordinate_system(0, 10, 0, 8)

# 2. Beispieldaten (Rohdaten)
# Diese Daten werden vom Histogramm automatisch gezählt
messwerte = [1.2, 1.7, 1.8, 2.2, 2.5, 2.9, 3.1, 3.5, 3.8, 3.9, 4.2, 5.5, 5.8, 8.2]

# 3. Histogramm einzeichnen
# Start bei 0, jede Säule ist 2 Einheiten breit (0-2, 2-4, 4-6, ...)
draw_histogram(ax, messwerte, bin_width=2, start_value=0, label="Häufigkeit", color='#2ecc71')

ax.legend()

# als eps oder png speichern  und anzeigen
# oder wie hier: Alles aufs Mal:
#save_system(fig, "histogramm1.eps")
#save_system(fig, "histogramm1.png")
plt.show()
