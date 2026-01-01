from plotting_lib import draw_pie_chart
import matplotlib.pyplot as plt

# Daten definieren
marken = ["Apple", "Huawei", "Samsung", "Andere"]
absatz = [3, 8, 2, 16]

# Diagramm zeichnen
draw_pie_chart(marken, absatz, mode="absolute", title="Marktanteile Handys")

plt.show()
