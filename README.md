# bora_wrapper

Cliente Python para consultar y extraer enlaces de avisos del **Boletín Oficial de la República Argentina (BORA)**. Actualmente soporta la búsqueda avanzada de la Segunda Sección (Sociedades y Avisos Judiciales).

---

## Requisitos previos

- [uv](https://docs.astral.sh/uv/) — gestor de entornos y dependencias
- Python ≥ 3.9

---

## Setup

### 1. Clonar el repo

```bash
git clone https://github.com/Ignacio-Ibarra/bora_wrapper
cd bora_wrapper
```

### 2. Instalar dependencias

```bash
uv sync
```

### 3. Configurar proxy (opcional)

Si trabajás detrás de un proxy corporativo, creá un `.env` en la raíz:

```env
PROXY_HOST=host.del.proxy
PROXY_PORT=8080
PROXY_USER=usuario
PROXY_PASS=password
```

Si las cuatro variables no están definidas, el wrapper se conecta sin proxy.

---

## Uso

### Como CLI

```bash
uv run bora-cli --start-date 28/05/2025 --end-date 28/05/2025 --rubros "CONSTITUCION SA"
```

| Flag | Descripción |
|---|---|
| `--start-date` | Fecha de inicio (formato `dd/mm/YYYY`) |
| `--end-date` | Fecha de fin (formato `dd/mm/YYYY`) |
| `--rubros` | Uno o varios rubros separados por `\|` (p. ej. `"CONSTITUCION SA\|CONTRATO SRL"`) |

El resultado se guarda en `output/links_<rubros>_<start>_<end>.json`. Si la búsqueda no devuelve resultados, se anexa una línea a `output/busqueda_vacia.txt`.

### Como librería

#### Búsqueda de avisos (Segunda Sección)

```python
from bora_wrapper import SegundaSeccion

busqueda = SegundaSeccion(
    rubros=["CONSTITUCION SA"],
    fecha_desde="28/05/2025",
    fecha_hasta="28/05/2025",
)
links = busqueda.get_result()
for link in links:
    print(link)
# https://www.boletinoficial.gob.ar/detalleAviso/segunda/A1396533/20250528?busqueda=1
# https://www.boletinoficial.gob.ar/detalleAviso/segunda/A1396535/20250528?busqueda=1
# ...
```

#### Listado de rubros disponibles

```python
from bora_wrapper import BusquedaRubros

rubros = BusquedaRubros(seccion="segunda").get_result()
print(rubros)
```

---

## Estructura del proyecto

```
bora_wrapper/
├── __init__.py         # API pública
├── cli.py              # Entry point del comando bora-cli
├── core.py             # BORA — cliente HTTP base
├── busqueda.py         # BusquedaAvanzadaSeccion, BusquedaRubros
└── secciones.py        # SegundaSeccion
```

---

## Tests

```bash
uv run pytest
```

Los tests offline corren por defecto. Para incluir el test e2e contra el BORA real:

```bash
uv run pytest --run-online
```

---

## Pendientes / Ideas futuras

- Agregar soporte para otras secciones (Primera, Tercera, Suplementos).
- Soporte de exportación a CSV además de JSON.
- Automatizar búsquedas diarias.

---

## Licencia

MIT. Ver [`LICENSE`](LICENSE).