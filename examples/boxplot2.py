#!/usr/bin/python3

# Boxplot Beispiel 2

from bmsw_graph_lib import b

# System erstellen (x-Achse für Noten oder Punkte, y-Achse als Stapelplatz)
b.draw_system(0, 20, 0, 6, show_y_axis=False)

# Beispieldaten: Punkte in einer Prüfung
daten_klasse_a = [3, 5, 6, 7, 8, 8, 9, 10, 12, 14]
daten_klasse_b = [5, 8, 9, 9, 10, 10, 11, 12, 13, 15, 19]

# Zwei Boxplots übereinander zeichnen
b.draw_boxplot(daten_klasse_a, y_position=2, label="Klasse A", color='#3498db', axis_label="Noten")
b.draw_boxplot(daten_klasse_b, y_position=4, label="Klasse B", color='#2ecc71')

# optional save:
#b.save_system("png")
b.show()
