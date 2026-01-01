# main.py
from plotting_lib import create_swiss_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt




# 1. System erstellen (z.B. -4 bis 4)
fig, ax = create_swiss_coordinate_system(-4, 4, -4, 4)

# 2. Eine hellblaue Parabel zeichnen: f(x) = 0.5 * x^2 - 2
draw_function_into_system(ax, lambda x: 0.5 * x**2 - 2, (-3.5, 3.5), label="Parabel", color='#ccddee')

# 3. Eine Gerade zeichnen: f(x) = x + 1
draw_function_into_system(ax, lambda x: x + 1, (-4, 3), label="Gerade")

# 4. Einen Punkt manuell hinzufügen (Beispiel für spätere Erweiterungen)
ax.plot(2  , 3  , 'ro'   ) # Ein roter Punkt bei (2,3)
ax.text(2.2, 2.9, 'P=(2|3)', color='red')

# weitere Punkt
ax.plot(2  , -1  , marker='s', color='#883366')
ax.text(2.2, -1.2, 'Q=(2|-1)', color='#883366')

# Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
save_system(fig, "function1.png")
save_system(fig, "function1.eps")

plt.show()
