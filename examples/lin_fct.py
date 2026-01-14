#!/usr/bin/python3
from bms_graph_lib import bmsw_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt


# A. System erstellen (z.B. -4 bis 4)
fig, ax = bmsw_coordinate_system(-6, 12, -5, 6)

# B. Zeichnen


dots = []

# 1. y=2/3 x + 2
draw_function_into_system(ax, lambda x: 2/3*x+2, (-5.5, 5.5), color="#ff0000")
# Punkte und Texte
dots.extend([[0,2],[3,4]])

# 2. y=-0.4 x + 3
draw_function_into_system(ax, lambda x: -0.4*x+3, (-5.5, 11.5), color="#008800")
# Punkte und Texte
dots.extend([[-5,5],[5,1],[10,-1]])


# 
for dot in dots:
	#print(dot)
	ax.plot(dot[0], dot[1], 'ko')
	

plt.show()
