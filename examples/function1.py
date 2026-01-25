#!/usr/bin/python3

from bmsw_graph_lib import b

# optional: Font-Size vergrößern
#b.set_fontsize(30)

# A. System erstellen (z.B. -4 bis 4)
b.bmsw_coordinate_system(-1, 4, -4, 2)

# Funktion definieren
def f(x):	return -0.5*(x-2)**2 + 1.5

# 1. Eine Parabel in Scheitelform
b.draw_function_into_system(f, (-1, 3.5), label="Parabel", color='#ccddee')

# 2. Scheitelpunkt und Text
b.dot(2, 1.5, 'bo') # Ein blauer (b) Punkt (o) bei (2, 1.5)
b.text(1.5, 1.7, 'S=(2.2|1.6)',color='#0000bb')

# 3. Legende anzeigen
b.legend(loc='upper left', bbox_to_anchor=(1, 1))

# anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
#b.save_system("pdf")
#b.save_sysetm("jpg")
#b.save_sysetm("svg")
# und anzeigen (optional, aber von Vorteil)
b.show()
