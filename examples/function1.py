#!/usr/bin/python3
from   bms_graph_lib     import create_swiss_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt


# A. System erstellen (z.B. -4 bis 4)
fig, ax = create_swiss_coordinate_system(-4, 4, -4, 4)

# B. Zeichnen

# 1. a) Eine hellblaue Parabel zeichnen: f(x) = 0.5 * x^2 - 2
draw_function_into_system(ax, lambda x: 0.5 * x**2 - 2, (-3.5, 3.5), label="Parabel", color='#ccddee')

# 1. b) eine rote Parabel
draw_function_into_system(ax, lambda x: -0.3 * x**2 +2*x+1, (-3.5, 3.5), label="Parabel", color='#ff0000')

# 1. c) Eine Gerade zeichnen: f(x) = x + 1
draw_function_into_system(ax, lambda x: x + 1, (-4, 3), label="Gerade")


# 2. Punkte und Texte

# 2. a) Einen Punkt manuell hinzufügen (Beispiel für spätere Erweiterungen)
ax.plot(2  , 3  , 'ro'   ) # Ein roter (r) Punkt (o) bei (2,3)
ax.text(2.2, 2.9, 'P=(2|3)', color='red')

# 2. b) weitere Punkt mit "sqare" markiert
ax.plot(2  , -1  , marker='s', color='#883366') # s=square
ax.text(2.2, -1.2, 'Q=(2|-1)', color='#883366')

# 2. c) Ein grünes Kreuz bei (-3 | 2)
ax.plot(-3, 2, 'gx')  # grünes Kreuz

# 3. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))


# C. anzeigen und (optional) speichern
#save_system(fig, "function1.png")
#save_system(fig, "function1.eps")
#save_system(fig, "function1.svg")
# und anzeigen (optional, aber von Vorteil)
plt.show()
