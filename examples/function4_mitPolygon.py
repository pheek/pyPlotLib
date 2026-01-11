#!/usr/bin/python3

from bms_graph_lib import bmsw_coordinate_system, draw_function_into_system, draw_polygon, save_system
import matplotlib.pyplot as plt

# A. System erstellen 
fig, ax = bmsw_coordinate_system(-3, +4, -4, +2)

def parabelInScheitelform(x):
	return -0.5*(x - 2)**2 + 1.5

# B 1. Eine Parabel in Scheitelform
draw_function_into_system(ax, parabelInScheitelform, (-2, 3.5), label="Parabel", color='#ccddee')

# B 2. Scheitelpunkt
ax.plot(2  , 1.5  , 'bo') # Ein blauer (b) Punkt (o) bei (2, 1.5)

# C Polygon
# C 1. Punkte definieren (z.B. ein Parallelogramm)
dreieck_punkte = [[1, 1], [2, 0], [3, 1]]

# C 2. Zeichnen
draw_polygon(ax, dreieck_punkte, color='#8e44ff', label="Fläche A")


# D 3. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# E anzeigen und (optional) speichern
#save_system(fig, "function4.png")
#ave_system(fig, "function4.eps")
# und anzeigen (optional, aber von Vorteil)
plt.show()
