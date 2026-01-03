#!/usr/bin/python3
from plotting_lib import create_swiss_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt


# A. System erstellen (z.B. x -3 bis +4 und y von -4 bis +3)
fig, ax = create_swiss_coordinate_system(-3, +4, -4, +3)

def parabelInScheitelform(x):
	return -0.5*(x-2)**2 + 1.5

# B 1. Eine rote Parabel in Scheitelform
draw_function_into_system(ax, parabelInScheitelform, (-2, 3.5), label="Parabel", color='#ccddee')

# B 2. Scheitelpunkt
ax.plot(2  , 1.5  , 'bo') # Ein blauer (b) Punkt (o) bei (2, 1.5)


# C 3. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))



# D anzeigen und (optional) speichern
#save_system(fig, "function3.png")
#ave_system(fig, "function3.eps")
# und anzeigen (optional, aber von Vorteil)
plt.show()
