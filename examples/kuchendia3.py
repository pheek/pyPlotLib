#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib

from bmsw_graph_lib import b

# Daten definieren
lieblingsfach = ["Französisch", "Mathematik", "Englisch", "Turnen", "Pause"]
anz_sbs       = [3, 8, 2, 9, 16] #sbs = Schülerinnen bzw. Schülerers

# Diagramm zeichnen
b.draw_pie_chart(lieblingsfach, anz_sbs, mode="none", title="Lieblingsfach")

## show and (optional) save
#b.save_system("png")
b.show()
