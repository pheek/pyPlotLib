#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

# Boxplot Beispiel
from bmsw_graph_lib import b

b.set_fontsize(22)

# System erstellen (x-Achse für Noten oder Punkte, y-Achse als Stapelplatz)
# figsize gibt das breitexhöhe Verhältnis an (Standard: 10:8, aber bei Boxplots besser 10:20)
b.draw_system(1, 16, 0, 2, show_y_axis=False, figsize=(10,2))

# Beispieldaten: Punkte in einer Prüfung
daten_klasse = [3, 5, 6, 7, 8, 8, 9, 10, 12, 14]

# Zwei Boxplots übereinander zeichnen
b.draw_boxplot(daten_klasse, y_position=1, label="Klasse", axis_label="Noten", height=1.6)

# optional save
#b.save_system("png")
b.show()
