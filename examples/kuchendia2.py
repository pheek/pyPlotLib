#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

from bmsw_graph_lib import b

# Daten definieren
geschmack        = ["Kirschen", "Banana", "Minze", "Schocklaat", "Apple", "Baumnuss"]
anzahl_probanden = [3, 8, 2, 16, 11, 5]

# Diagramm zeichnen
b.draw_pie_chart(geschmack, anzahl_probanden, mode="relativ", title="Geschmacksrichtung")

## save (optional) and show
#b.save_system("svg")
b.show()
