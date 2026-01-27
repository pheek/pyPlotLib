#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

from bmsw_graph_lib import b


# A. System erstellen (z.B. -4 bis 4)
b.draw_system(-6, 12, -5, 6)

# B. Zeichnen
# dots definieren (python array of dots)
dots = []

# 1. y=2/3 x + 2
b.draw_function_into_system(lambda x: 2/3*x+2, (-5.5, 5.5), color="#ff0000")
# Punkte
dots.extend([[0,2],[3,4]]) # füge der leeren Liste zwei Punkte hinzu

# 2. y=-0.4 x + 3
b.draw_function_into_system(lambda x: -0.4*x+3, (-5.5, 11.5), color="#008800")
# Punkte
dots.extend([[-5,5],[0,3],[5,1],[10,-1]]) # füge weitere Punkte hinzu

# 3. y=-1/3x + 5
b.draw_function_into_system(lambda x: -0.3333*x+5, (-3, 11.5), color="#0000cc")
# Punkte
dots.extend([[-3,6],[0,5],[3,4],[6,3],[9,2]])

# 4. y=-3x-4
b.draw_function_into_system(lambda x: -3*x-4, (-3.2, 0.2), color="#cc00cc")
# Punkte
dots.extend([  [-3,5],  [-2,2] , [-1,-1]])

# 5. y=-3
b.draw_function_into_system(lambda x: -3+0*x, (-5.5, 11.5), color="#33ee00")
# Punkte
dots.extend([  [-5,-3],  [-2,-3] , [2,-3], [5, -3], [8, -3]])

# 6. y=0.3x-3
b.draw_function_into_system(lambda x: 0.25*x-0.5, (-5.5, 11.5), color="orange")
# Punkte
dots.extend([ [-2,-1], [6, 1] ])

# 7. y=6/7x-2
b.draw_function_into_system(lambda x: x/7*6-2, (-3, 9), color="#aa7700")
# Punkte
dots.extend([ [0,-2], [7,4]])

# 8. y=-3/5x
b.draw_function_into_system(lambda x: -x/5*3, (-5.5, 7.5), color="#ff00cc")
# Punkte
dots.extend([ [-5,3], [5,-3]])


# draw all dots 
for dot in dots:
	b.dot(dot[0], dot[1], 'ko')

#optional speichern
#b.save_system('png')
b.show()
