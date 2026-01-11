#!/usr/bin/python3

# Boxplot Beispiel

from bms_graph_lib import bmsw_coordinate_system, draw_boxplot,save_system
import matplotlib.pyplot as plt

# System erstellen (x-Achse für Noten oder Punkte, y-Achse als Stapelplatz)
fig, ax = bmsw_coordinate_system(0, 20, 0, 4, show_y_axis=False)

# Beispieldaten: Punkte in einer Prüfung
daten_klasse = [3, 5, 6, 7, 8, 8, 9, 10, 12, 14]

# Zwei Boxplots übereinander zeichnen
draw_boxplot(ax, daten_klasse, y_position=2, label="Klasse", color='#3498db', axis_label="Noten")

#save_system(fig, "boxplot1.png")
plt.show()
