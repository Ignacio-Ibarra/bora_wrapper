from bora import SegundaSeccion

segunda_seccion = SegundaSeccion(rubros=['AVISOS COMERCIALES'], fecha_desde="28/05/2025", fecha_hasta="28/05/2025")
links = segunda_seccion.get_result()
print(f"Se han encontrado {len(links)} resultados\n")
for link in links:
    print(link)