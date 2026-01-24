#!/usr/bin/python3

from bmsw_graph_lib import b

# 1. System erstellen, das bei 0 startet (z.B. bis x=6, y=5)
# Wir geben -1 als Min an, damit die Achsen nach links/unten noch etwas Platz haben
b.bmsw_coordinate_system(0, 6, 0, 5)

# 2. Daten definieren
monate_x = [1, 2, 3, 4, 5]
werte_y  = [2, 4, 3, 5, 4]

# 3. Säulen zeichnen
b.draw_bar_chart(monate_x, werte_y, label="Verkäufe", color='#fabc22')

b.legend()

# anzeigen und (optional) speichen
#b.save_system("barchart1.png")
#b.save_system("barchart1.eps")

b.show()


