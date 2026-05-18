import json

import pytest

from bora_wrapper import SegundaSeccion


def test_segunda_seccion_builds_payload():
    instancia = SegundaSeccion(
        rubros=["CONSTITUCION SA"],
        fecha_desde="28/05/2025",
        fecha_hasta="28/05/2025",
    )
    params = json.loads(instancia.payload["params"])
    assert params["rubros"] == ["CONSTITUCION SA"]
    assert params["fechaDesde"] == "28/05/2025"
    assert params["fechaHasta"] == "28/05/2025"
    assert params["seccion"] == [2]
    assert instancia.seccion == "segunda"


@pytest.mark.online
def test_get_result_returns_list():
    """Test e2e: requiere acceso al BORA. Correr con: pytest --run-online"""
    instancia = SegundaSeccion(
        rubros=["CONSTITUCION SA"],
        fecha_desde="28/05/2025",
        fecha_hasta="28/05/2025",
    )
    resultado = instancia.get_result()
    assert isinstance(resultado, list)
    for item in resultado:
        assert isinstance(item, str)
        assert item.startswith("https://")
