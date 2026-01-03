#!/usr/bin/python3
from plotting_lib import create_swiss_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt


# A. System erstellen (z.B. -4 bis 4)
fig, ax = create_swiss_coordinate_system(-4, 4, -4, 4)


# 1. Eine hellblaue Parabel zeichnen: f(x) = 0.5 * x^2 - 2
draw_function_into_system(ax, lambda x: 0.5 * x**2 - 2, (-3.5, 3.5), label="Parabel", color='#ccddee')

draw_function_into_system(ax, lambda x: -0.3 * x**2 +2*x+1, (-3.5, 3.5), label="Parabel", color='#ff0000')

# 2. Eine Gerade zeichnen: f(x) = x + 1
draw_function_into_system(ax, lambda x: x + 1, (-4, 3), label="Gerade")

# 3. Einen Punkt manuell hinzufügen (Beispiel für spätere Erweiterungen)
ax.plot(2  , 3  , 'ro'   ) # Ein roter (r) Punkt (o) bei (2,3)
ax.text(2.2, 2.9, 'P=(2|3)', color='red')

# 4. weitere Punkt
ax.plot(2  , -1  , marker='s', color='#883366') # s=square
ax.text(2.2, -1.2, 'Q=(2|-1)', color='#883366')

# 5. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))



# speichern und anzeigen (optional)
save_system(fig, "function1.png")
save_system(fig, "function1.eps")
# und anzeigen (optional, aber von Vorteil)
plt.show()
