#!/usr/bin/python3

from bmsw_graph_lib import b

# A. System erstellen 
b.draw_system(-1, +4, -1, +3)

def wurzelFunktion(x):
	return 1.5 * b.sqrt(x)

# B 1. Eine Parabel in Scheitelform
b.draw_function_into_system(wurzelFunktion, (0, 3.5), label="Parabel", color='#ccddee')

# B Polygon
#   Punkte definieren (z.B. ein Parallelogramm)
xx = 2.75
dreieck_punkte = [[0,0], [xx, 0], [xx, wurzelFunktion(xx)]]

# C Zeichnen
b.draw_polygon(dreieck_punkte, color='#8e44ff', label="Fläche A")

# D Eckpunkte Beschriften
labels = ["", "B", "C"]
for i, p in enumerate(dreieck_punkte):
    b.text(p[0] + 0.12, p[1] + 0.02, labels[i], fontweight='bold', ha='center')

# E Legende anzeigen
b.legend(loc='upper left')

# F anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
# und anzeigen (optional, aber von Vorteil)
b.show()
