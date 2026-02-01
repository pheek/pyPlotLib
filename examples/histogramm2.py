#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

from bmsw_graph_lib import b

# 1. System erstellen (z.B. von 0 bis 10 auf beiden Achsen)
b.draw_system(0, 31, 0, 11, step_x=5)

# 2. Beispieldaten (Rohdaten)
# Diese Daten werden vom Histogramm automatisch gezählt
messwerte = [5.5, 5.8, 8.2, 11.6, 11.6, 11.6, 15.6, 8.7, 21.8, 25.3]

# 3. Histogramm einzeichnen
# Start bei 0, jede Säule ist 2 Einheiten breit (0-2, 2-4, 4-6, ...)
b.draw_histogram(messwerte, bin_width=5, start_value=0, label="Häufigkeit")

b.legend()

# save (optional) and show
#b.save_system("png")
b.show()
