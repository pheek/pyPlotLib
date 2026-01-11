#!/usr/bin/python3

from bms_graph_lib import bmsw_coordinate_system, draw_function_into_system, draw_polygon, save_system
import matplotlib.pyplot as plt

# A. System erstellen 
fig, ax = bmsw_coordinate_system(-1, +4, -1, +3)

def wurzelFunktion(x):
	return x**0.5 # wurzel

# B 1. Eine Parabel in Scheitelform
draw_function_into_system(ax, wurzelFunktion, (0, 3.5), label="Parabel", color='#ccddee')

# B Polygon
# B 1. Punkte definieren (z.B. ein Parallelogramm)
xx = 3.5
dreieck_punkte = [[0,0], [xx, 0], [xx, wurzelFunktion(xx)]]

# C 2. Zeichnen
draw_polygon(ax, dreieck_punkte, color='#8e44ff', label="Fläche A")

# D 3. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# E anzeigen und (optional) speichern
#save_system(fig, "function4.png")
#ave_system(fig, "function4.eps")
# und anzeigen (optional, aber von Vorteil)
plt.show()
