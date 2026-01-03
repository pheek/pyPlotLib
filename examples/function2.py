
#!/usr/bin/python3
from plotting_lib import create_swiss_coordinate_system, draw_function_into_system, save_system
import matplotlib.pyplot as plt


# A. System erstellen (z.B. -4 bis 4)
fig, ax = create_swiss_coordinate_system(-3, 4, -4, 3)


# 1. Eine rote Parabel in Scheitelform
draw_function_into_system(ax, lambda x: -0.5*(x-2)**2 + 1.5, (-2, 3.5), label="Parabel", color='#ccddee')

# 2. Scheitelpunkt
ax.plot(2  , 1.5  , 'bo') # Ein blauer (b) Punkt (o) bei (2, 1.5)


# 3. Legende anzeigen
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))



# speichern und anzeigen (optional)
save_system(fig, "function2.png")
save_system(fig, "function2.eps")
# und anzeigen (optional, aber von Vorteil)
plt.show()
