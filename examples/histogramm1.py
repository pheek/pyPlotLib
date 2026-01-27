#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

from bmsw_graph_lib import b

# 1. System erstellen (z. B. von 0 bis 10 auf beiden Achsen)
b.draw_system(0, 10, 0, 8)

# 2. Beispieldaten (Rohdaten)
# Diese Daten werden vom Histogramm automatisch gezählt
messwerte = [1.2, 1.7, 1.8, 2.2, 2.5, 2.9, 3.1, 3.5, 3.8, 3.9, 4.2, 5.5, 5.8, 8.2]

# 3. Histogramm einzeichnen
# Start bei 0, jede Säule ist 2 Einheiten breit (0-2, 2-4, 4-6, ...)
b.draw_histogram(messwerte, bin_width=2, start_value=0, label="Anzahl Qräx", color='#2ecc71')

b.legend()
# als eps oder png speichern  und anzeigen
# oder wie hier: Alles aufs Mal:
#b.save_system("eps")
#b.save_system("png")
b.show()
