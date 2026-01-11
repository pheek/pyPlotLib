#!/usr/bin/python3
from bms_graph_lib import draw_pie_chart, save_system
import matplotlib.pyplot as plt

# Daten definieren
marken = ["Apple", "Huawei", "Samsung", "Andere"]
absatz = [3, 8, 2, 16]

# Diagramm zeichnen
fig, ax = draw_pie_chart(marken, absatz, mode="absolute", title="Marktanteile Handys")

# optional speichern
#save_system(fig, "kuchendia1.png")
# anzeigen:
plt.show()
