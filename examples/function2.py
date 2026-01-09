#!/usr/bin/python3

from bms_graph_lib import bmsw_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt

# A. System erstellen (z.B. -4 bis 4)
fig, ax = bmsw_coordinate_system(-3, 4, -4, 3)

# 1. Eine Parabel in Scheitelform
draw_function_into_system(ax, lambda x: -0.5*(x-2)**2 + 1.5, (-2, 3.5), label="Parabel", color='#ccddee')

# 2. Scheitelpunkt
ax.plot(2, 1.5, 'bo') # Ein blauer (b) Punkt (o) bei (2, 1.5)

# 3. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# anzeigen und (optional) speichern
#save_system(fig, "function2.png")
#save_system(fig, "function2.eps")
#save_system(fig, "funciotn2.pdf")
# und anzeigen (optional, aber von Vorteil)
plt.show()
