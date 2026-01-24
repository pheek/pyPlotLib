#!/usr/bin/python3

from bmsw_graph_lib import b

# 1. System erstellen 
b.bmsw_coordinate_system(0, 6, 0, 6)

# 2. Daten definieren
pos_x = [1, 2, 3, 4, 5]
groessen = ["XS", "S", "M", "L", "XL"]
anzahl = [1, 3, 5, 4, 2]

# 3. Säulen zeichnen
b.draw_bar_chart(pos_x, anzahl, color='#8e44ad') # Ein schönes Violett

# 4. Namen statt Zahlen an die x-Achse schreiben
b.set_custom_labels(pos_x, groessen)

# 5. Labels beschriften
b.ax.set_xticklabels(groessen, fontweight='bold', ha='right')

# 6. Legende zeichnen
b.legend(["Verkäufe"])

## save (optional) and show
#b.save_system("barchart2.png")
b.show()
