# 📰 `bora_wrapper`: Scraper del Boletín Oficial de la República Argentina

Este proyecto permite consultar y extraer enlaces del Boletín Oficial de la República Argentina (BORA), específicamente de la Segunda Sección (Sociedades y Avisos Judiciales).

## 🚀 Características

- Inicializa una sesión con cookies para evitar bloqueos.
- Realiza búsquedas avanzadas por rubro y fecha con manejo de paginación.
- Extrae URLs directas de las publicaciones.

## ⚙️ Instalación y Configuración

Este proyecto utiliza [uv](https://github.com/astral-sh/uv) para la gestión de dependencias y entornos.

**1. Clonar el repo:**
```bash
git clone [https://github.com/Ignacio-Ibarra/bora_wrapper](https://github.com/Ignacio-Ibarra/bora_wrapper)
cd bora_wrapper
```

## 🗂 Estructura del proyecto
```

```

## ⚙️ Requisitos

- Python >= 3.9
- `requests`
- `beautifulsoup4`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

## 💡 Ejemplo de uso

Ejecución por consola, guarda resultado en carpeta `output/`

```bash
python run.py --start-date 01/01/2024 --end-date 29/06/2024 --rubro "CONSTITUCION SA"
```

O reutilizando el código. 

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

## 📌 Pendientes / Ideas futuras
* Agregar soporte para otras secciones (Primera, Tercera, Suplementos).

* Exportar resultados a CSV/JSON.

* Automatizar búsquedas diarias.

## 📝 Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE] para más detalles.

## 🙌 Agradecimientos
Boletín Oficial por su acceso público a datos.



