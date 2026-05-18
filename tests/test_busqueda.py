import json

from bora_wrapper.busqueda import inject_page


def test_inject_page_replaces_existing_key():
    payload = json.dumps({"numeroPagina": 1, "rubros": ["X"]})
    result = json.loads(inject_page(page=3, key="numeroPagina", json_string=payload))
    assert result["numeroPagina"] == 3
    assert result["rubros"] == ["X"]


def test_inject_page_adds_missing_key():
    payload = json.dumps({"rubros": ["X"]})
    result = json.loads(inject_page(page=5, key="numeroPagina", json_string=payload))
    assert result["numeroPagina"] == 5
