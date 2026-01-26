#!/usr/bin/python3

from bmsw_graph_lib import b

# optional: Font-Size vergrößern
#b.set_fontsize(20)

# A. System erstellen (z.B. -4 bis 4)
b.draw_system(-1, 4, -4, 2)

# Funktion definieren
def f(x):
	return -0.5 * (x - 2)**2 + 1.5

# Eine Parabel in Scheitelform
b.draw_function_into_system(f, (-0.5, 3.5))

# Legende anzeigen (optional)
#b.legend(loc='lower center')

# anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
#b.save_system("pdf")
#b.save_sysetm("jpg")
#b.save_sysetm("svg")
# und anzeigen (optional, aber von Vorteil)
b.show()
