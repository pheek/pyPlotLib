#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib


from bmsw_graph_lib import b

# 1. System erstellen 
b.draw_system(0, 7, 0, 22, grid_x=1, step_x=1, grid_y=1, step_y=5)

# Wird set_fontsize vor "draw_system" aufgerufen, so
# werden auch die Achsenbeschriftungen vergrößert
b.set_fontsize(16)

# 2. Daten definierensave_system(fig, "barchart1.png")

pos_x = [1, 2, 3, 4, 5, 6, 7]
groessen = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
anzahl = [10, 20, 15, 4, 7, 7, 11]

# 3. Säulen zeichnen
b.draw_bar_chart(pos_x, anzahl, color='#8e2288') # Ein schönes Violett

# 4. Namen statt Zahlen an die x-Achse schreiben
b.set_custom_labels(pos_x, groessen)

b.text(-0.5, 6, 'Relative Häufigkeit in %', color='#000000', rotation=90)

#optional:
#evtl schief stellen
b.ax.set_xticklabels(groessen, fontweight='bold', rotation=30, ha='right')

#b.legend(["Menusalate"], loc='upper center')

## save (optional) and show
#b.save_system("png")
b.show()
