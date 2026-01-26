#!/usr/bin/python3

from bmsw_graph_lib import b

# System erstellen 
b.draw_system(-1, +4, -1, +3)

# Funktion definieren
def wurzelFunktion(x):
	return 1.5 * b.sqrt(x)

# Funktion zeichnen mit label in LaTeX
b.draw_function_into_system(wurzelFunktion, (0, 3.5), label=r'$1.5\sqrt{x}$', color='#ccddee')

# Polygon
#   Punkte definieren (z.B. ein Parallelogramm)
xx = 2.75
dreieck_punkte = [[0,0], [xx, 0], [xx, wurzelFunktion(xx)]]

# Polygon zeichnen
flaechenfarbe = "#8e44ff"
b.draw_polygon(dreieck_punkte, color=flaechenfarbe, label="Fläche A")

# Eckpunkte Beschriften
labels = ["", "P", "Q"]
for i, p in enumerate(dreieck_punkte):
    b.text(p[0] + 0.12, p[1] + 0.02, labels[i], fontweight='bold', ha='center')

# Flärhe beschritfen
b.text(1.75, 0.5, "A", color=flaechenfarbe)
    
# Legende anzeigen
b.legend(loc='upper left')

# F anzeigen und (optional) speichern
#b.save_system("png")
#b.save_system("eps")
# und anzeigen (optional, aber von Vorteil)
b.show()
