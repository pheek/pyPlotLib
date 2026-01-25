#!/usr/bin/python3

from bmsw_graph_lib import b

# A. System erstellen 
b.draw_system(-3, +4, -4, +2)

def parabelInScheitelform(x):
	return -0.5*(x - 2)**2 + 1.5

# B 1. Eine Parabel in Scheitelform
b.draw_function_into_system(parabelInScheitelform, (-2, 3.5), label="Parabel", color='#ccddee')

# B 2. Scheitelpunkt
b.dot(2  , 1.5  , 'bo') # Ein blauer (b) Punkt (o) bei (2, 1.5)

# C Polygon
# C 1. Punkte definieren (z.B. ein Parallelogramm)
dreieck_punkte = [[1, 1], [2, 0], [3, 1]]

# C 2. Zeichnen
b.draw_polygon(dreieck_punkte, color='#8e44ff', label="Fläche A")


# D 3. Legende anzeigen
b.legend(loc='upper left')

# E anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
# und anzeigen (optional, aber von Vorteil)
b.show()
