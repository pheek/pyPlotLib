#!/usr/bin/python3

# Boxplot Beispiel
from bmsw_graph_lib import b

# System erstellen (x-Achse für Noten oder Punkte, y-Achse als Stapelplatz)
b.bmsw_coordinate_system(0, 20, 0, 4, show_y_axis=False)

# Beispieldaten: Punkte in einer Prüfung
daten_klasse = [3, 5, 6, 7, 8, 8, 9, 10, 12, 14]

# Zwei Boxplots übereinander zeichnen
b.draw_boxplot(daten_klasse, y_position=2, label="Klasse", color='#3498db', axis_label="Noten")

# optional save
#b.save_system("boxplot1.png")
b.show()
