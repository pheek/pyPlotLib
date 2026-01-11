#!/usr/bin/python3

from bms_graph_lib import bmsw_coordinate_system, draw_function_into_system, draw_polygon, save_system
import matplotlib.pyplot as plt

# A. System erstellen 
fig, ax = bmsw_coordinate_system(-1, +4, -1, +3)

def wurzelFunktion(x):
	return 1.5 * x**0.5 # wurzel

# B 1. Eine Parabel in Scheitelform
draw_function_into_system(ax, wurzelFunktion, (0, 3.5), label="Parabel", color='#ccddee')

# B Polygon
#   Punkte definieren (z.B. ein Parallelogramm)
xx = 2.75
dreieck_punkte = [[0,0], [xx, 0], [xx, wurzelFunktion(xx)]]

# C Zeichnen
draw_polygon(ax, dreieck_punkte, color='#8e44ff', label="Fläche A")

# D Eckpunkte Beschriften
labels = ["", "B", "C"]
for i, p in enumerate(dreieck_punkte):
    ax.text(p[0] + 0.12, p[1] + 0.02, labels[i], fontweight='bold', ha='center')

# E Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# F anzeigen und (optional) speichern
#save_system(fig, "function4.png")
#ave_system(fig, "function4.eps")
# und anzeigen (optional, aber von Vorteil)
plt.show()
