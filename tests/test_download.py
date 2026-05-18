from bora_wrapper.texts.download import get_endpoint


def test_get_endpoint_builds_url():
    assert (
        get_endpoint("segunda", "A1396533", "20250528")
        == "/detalleAviso/segunda/A1396533/20250528?busqueda=1"
    )
