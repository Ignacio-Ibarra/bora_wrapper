from bora import SegundaSeccion

segunda_seccion = SegundaSeccion(rubros=['CONSTITUCION SA'], fecha_desde="28/05/2025", fecha_hasta="28/05/2025")
links = segunda_seccion.get_result()
for link in links:
    print(link)