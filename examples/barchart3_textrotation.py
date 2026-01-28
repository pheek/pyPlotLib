#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib


from bmsw_graph_lib import b

# 1. System erstellen 
b.draw_system(0, 7, 0, 9)

# 2. Daten definierensave_system(fig, "barchart1.png")

pos_x = [1, 2, 3, 4, 5, 6]
groessen = ["extra small", "small", "medium", "large", "extra large", "bombastic"]
anzahl = [1, 3, 5, 4, 2, 8]

# 3. Säulen zeichnen
b.draw_bar_chart(pos_x, anzahl, color='#8e2288') # Ein schönes Violett

# 4. Namen statt Zahlen an die x-Achse schreiben
b.set_custom_labels(pos_x, groessen)

#optional:
#evtl schief stellen
b.ax.set_xticklabels(groessen, fontweight='bold', rotation=60, ha='right')

b.legend(["Verkäufe Autos"], loc='upper center')

## save (optional) and show
#b.save_system("png")
b.show()
