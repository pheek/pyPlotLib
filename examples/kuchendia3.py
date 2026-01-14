#!/usr/bin/python3
from bms_graph_lib import draw_pie_chart, save_system
import matplotlib.pyplot as plt

# Daten definieren
lieblingsfach = ["Französisch", "Mathematik", "Englisch", "Turnen", "Pause"]
anz_sbs       = [3, 8, 2, 9, 16]

# Diagramm zeichnen
fig, ax = draw_pie_chart(lieblingsfach, anz_sbs, mode="none", title="Lieblingsfach")

## show and (optional) save
#save_system(fig, "kuchendia3.png")
plt.show()
