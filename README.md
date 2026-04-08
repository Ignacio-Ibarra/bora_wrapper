# `bora_wrapper`: Scraper del Boletín Oficial de la República Argentina

Este proyecto permite consultar y extraer enlaces del Boletín Oficial de la República Argentina (BORA), específicamente de la Segunda Sección (Sociedades y Avisos Judiciales).

## 🚀 Características

- **Gestión de Sesiones:** Manejo automático de cookies para navegar sin bloqueos.
- **Búsqueda Avanzada:** Filtrado por rubros, fechas y manejo de paginación compleja.
- **CLI Integrado:** Ejecución directa desde la terminal mediante `uv`.
- **Modular:** Estructura limpia para extender a otras secciones (Primera o Tercera).

## Instalación y Configuración

Este proyecto utiliza [uv](https://github.com/astral-sh/uv) para la gestión de dependencias y entornos.

**1. Clonar el repo:**
```bash
git clone [https://github.com/Ignacio-Ibarra/bora_wrapper](https://github.com/Ignacio-Ibarra/bora_wrapper)
cd bora_wrapper
```

**2. Sincronizar el entorno:**
```bash
# Si usas tu Python local (recomendado en entornos corporativos)
uv venv --python python
uv sync
```

## Uso

## Interfaz de Línea de Comandos (CLI)

Gracias a la configuración de pyproject.toml, puedes usar el comando bora-cli (vía uv run):

```bash
uv run bora-cli --start-date 01/01/2024 --end-date 29/06/2024 --rubro "CONSTITUCION SA"
```

## Como librería

```python
from bora import SegundaSeccion

# Buscar contrataciones del 28 de mayo de 2025 con rubro específico
busqueda = SegundaSeccion(
    rubros=['CONSTITUCION SA'], 
    fecha_desde="28/05/2025", 
    fecha_hasta="28/05/2025"
)
resultados = busqueda.get_result()

for link in resultados:
    print(link)

# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396533/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396535/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396537/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396538/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396540/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396541/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396542/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396543/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396544/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396545/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396546/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396548/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396550/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396551/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396552/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396553/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396554/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396555/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396557/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396558/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396559/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396560/20250528?busqueda=1
# https://www.boletinoficial.gov.ar/detalleAviso/segunda/A1396561/20250528?busqueda=1
```

## Estructura del Proyecto

* `bora/`: Paquete principal con la lógica de scraping y sesiones.

* `run.py`: Punto de entrada para la ejecución por consola.

* `pyproject.toml`: Definición de dependencias y scripts del proyecto.

* `output/`: Carpeta (generada automáticamente) donde se guardan los resultados.

## Requisitos

- Python >= 3.9
- `requests`
- `beautifulsoup4`

## Desarrollo y Contribución

Si quieres agregar soporte para nuevas secciones:

* Revisa `bora/core.py` para entender la base de las peticiones.

* Implementa la lógica específica en un nuevo archivo dentro de bora/.

## 📌 Pendientes / Ideas futuras
* Agregar soporte para otras secciones (Primera, Tercera, Suplementos).

* Exportar resultados a CSV/JSON.

* Automatizar búsquedas diarias.

## 📝 Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE] para más detalles.

## 🙌 Agradecimientos
Boletín Oficial por su acceso público a datos.



