#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

from bmsw_graph_lib import b

# System erstellen (z.B. -4 bis 4)
b.draw_system(-1, 4, -3, 1)


# Eine Wurzel
b.draw_function_into_system(lambda x: b.sqrt(x) - yyy, (0, 3.5), label="Wurzel", color='#ccddee')

	
b.dot(0, -1.5)

b.legend()

# anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
#b.save_system("pdf")
#b.save_sysetm("jpg")
# und anzeigen (optional, aber von Vorteil)
b.show()
