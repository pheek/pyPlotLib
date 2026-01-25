#!/usr/bin/python3
from bmsw_graph_lib import b

# Daten definieren
marken = ["Apple", "Huawei", "Samsung", "Andere"]
absatz = [3, 8, 2, 16]

# Diagramm zeichnen
b.draw_pie_chart(marken, absatz, mode="absolute", title="Marktanteile Handys")

# optional speichern
#b.save_system("png")
# anzeigen:
b.show()
