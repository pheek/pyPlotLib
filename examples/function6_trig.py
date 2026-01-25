#!/usr/bin/python3

from bmsw_graph_lib import b

# Optional set Font Size
b.set_fontsize(20)

# A. System erstellen (z.B. -4 bis 4)
b.draw_system(-3, 6.2, -2, 1, trig=True)

# Funktion definieren
def f(x):	return b.cos(x) - 0.5

# 1. Eine Parabel in Scheitelform
b.draw_function_into_system(f, (-3, 6), label="Cosinus verschoben", color='#ccddee')

b.set_trig_labels()

# 2. Scheitelpunkt und Text
b.labeled_dot(3.14, -1.5, label=r'$x \mapsto \cos(x) - \frac{1}{2}$', color="#000066")

# 3. Legende anzeigen
b.legend(loc='upper right')

# anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
#b.save_system("pdf")
#b.save_sysetm("jpg")
#b.save_sysetm("svg")
# und anzeigen (optional, aber von Vorteil)
b.show()
