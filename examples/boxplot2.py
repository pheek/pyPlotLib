#!/usr/bin/python3

# Boxplot Beispiel

from bms_graph_lib import bmsw_coordinate_system, draw_boxplot,save_system
import matplotlib.pyplot as plt

# System erstellen (x-Achse für Noten oder Punkte, y-Achse als Stapelplatz)
fig, ax = bmsw_coordinate_system(0, 20, 0, 6, show_y_axis=False)

# Beispieldaten: Punkte in einer Prüfung
daten_klasse_a = [3, 5, 6, 7, 8, 8, 9, 10, 12, 14]
daten_klasse_b = [5, 8, 9, 9, 10, 10, 11, 12, 13, 15, 19]

# Zwei Boxplots übereinander zeichnen
draw_boxplot(ax, daten_klasse_a, y_position=2, label="Klasse A", color='#3498db', axis_label="Noten")
draw_boxplot(ax, daten_klasse_b, y_position=4, label="Klasse B", color='#2ecc71')

#save_system(fig, "boxplot2.png")
plt.show()
