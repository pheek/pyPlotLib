bmsw_graph_lib.py
=================

(c) 01_01_2026 philipp.freimann@bms-w.ch                                      
    (with help of gemini.google.com)
		
 Das Schweizer Koordinatensystem hat Pfeile, die über das Gitter hinausragen,  
 was beim standard-Plott (mathplotilb/gnuplot/geogebra) nicht der Fall ist.    
                                                                               
 Mit dieser Library sind möglich:                                              
 *  Koordinatensysteme
	   (Kartesisch, mit und ohne y-Achse auch mit trigonometrischer x-Achse)
     ((noch) keine Polarkoordinaten)
		 
 *  Funktionen Graphen mit Definitionsbereich und Funktionen aus der
              python-numpy Librariy
 *  Texte                                                                       
 *  Linien                                                                      
 *  Punkte                                                                      
 *  Diagrammarten:
    + Bar-Chart                                                               
    + Histogramm                                                              
    + Boxplot                                                                 
   Beim Boxplot beachten, dass "show_y_axis=False" gesetzt werden muss, denn   
   beim Boxplot macht die y-Achse keinen Sinn.                                 

Koordinatensysteme
------------------
Einfaches Koordinatensystem von Koordinatensystem mit einf

![Beispil Koordinatensystem](https://github.com/pheek/pyPlotLib/blob/main/examples/img/koordinatensystem1.png)

code:

```
from bmsw_graph_lib import b

b.draw_system(-4, 4, -3, 3) # show_y_axis=True = default

b.show()
```

Koordinatensysteme sind auch mit trigonometrischer x-Achse möglich:

![Beispil Koordinatensystem](https://github.com/pheek/pyPlotLib/blob/main/examples/img/koordinatensystem1.png)

Dazu ist einfach der Parameter "trig=True" zu setzen:

```
from bmsw_graph_lib import b

b.draw_system(0, 6, -0.5, 2.5, trig=True) # show_y_axis=True = default

b.show()
```


Funktionen
----------
![Beispil Funktion](https://github.com/pheek/pyPlotLib/blob/main/examples/img/funktion1.png)

Eine einfache Funktion wird mit Funktionsterm und Definitionsbereich in ein Koordinatensystem eingezeichnet:

```
from bmsw_graph_lib import b
b.draw_system(-1, 4, -4, 2)

# Funktion y=-0.5(x-2)^2 + 1.5 definieren:
def f(x):
	return -0.5 * (x - 2)**2 + 1.5

# zeichnen im Definitionsbereich x von -0.5 bis 3.5:
b.draw_function_into_system(f, (-0.5, 3.5))
''

# und anzeigen (optional, aber von Vorteil)
b.show()
```