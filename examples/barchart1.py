#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib


from bmsw_graph_lib import b

#optional set Font Size
#b.set_fontsize(20)

# 1. System erstellen, das bei 0 startet (z.B. bis x=6, y=5)
# Wir geben -1 als Min an, damit die Achsen nach links/unten noch etwas Platz haben
b.draw_system(0, 6, 0, 5)

# 2. Daten definieren
monate_x     = [1, 2, 3, 4, 5]
verkaeufe_y  = [2, 4, 3, 5, 4]

# 3. Säulen zeichnen
# number_shift (default = 0.5) bedeutet: Wie hoch über der Säule soll die Zahl beschriftet werden
b.draw_bar_chart(monate_x, verkaeufe_y, label="Verkäufe", number_shift=0.2)

b.legend()

# anzeigen und (optional) speichen
#b.save_system("png")
#b.save_system("eps")
#b.save_sysetm("pdf")

b.show()
