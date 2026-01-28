#!/usr/bin/python3
# see https://github.com/pheek/pyPlotLib


from bmsw_graph_lib import b

#optional Font Size:
#b.set_fontsize(20)

# A. System erstellen (z.B. -4 bis 4)
b.draw_system(-4, 4, -4, 5)

# B. Zeichnen

# Eine blaue Parabel zeichnen: f(x) = 0.5 * x^2 - 2
# optional: "label"
b.draw_function_into_system(lambda x: 0.5 * x**2 - 2, (-3.5, 3.5), label="Parabel blau")

# Eine rote Parabel
# optional "farbe)
b.draw_function_into_system(lambda x: b.log(x), (0.01, 3.5), label="log(): rot", color='#ff0000')

# Punkte und Texte

# Einen Punkt manuell hinzufügen (Beispiel für spätere Erweiterungen)
b.dot (2, 3) # Ein blauer Punkt (default)
b.text(2.2, 3.1, 'P = (2|3)', color='#ff0000')

b.dot(-1, 3, 'xr') #rotes kreuz (r=rot, x=kreuz)

# weitere Punkt
b.dot (2  , -1  , marker='s'  , color='#883366') # s=square
b.text(2.2, -1.3, 'Q = (2|-1)', color='#883366')

# Bezeihcenter Punkt
b.labeled_dot(-3, 2, 'B', color="#cc6600")

# 3. Legende anzeigen
#eg. b.legend(loc='center', bbox_to_anchor=(1, 1))
b.legend(loc='lower right')

# C. speichen (optional) anzeigen
#b.save_system("png")
#b.save_system("eps")
#b.save_system("svg")
#b.save_system("pdf")
b.show()
