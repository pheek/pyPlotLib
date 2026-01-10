#!/usr/bin/python3
from bms_graph_lib import draw_pie_chart, save_system
import matplotlib.pyplot as plt

# Daten definieren
geschmack        = ["Kirschen", "Banana", "Minze", "Schocklaat", "Apple", "Baumnuss"]
anzahl_probanden = [3, 8, 2, 16, 11, 5]

# Diagramm zeichnen
fig, ax = draw_pie_chart(geschmack, anzahl_probanden, mode="relativ", title="Geschmacksrichtung")

## save (optional) and show
#save_system(fig, "kuchendia2.svg")
plt.show()
