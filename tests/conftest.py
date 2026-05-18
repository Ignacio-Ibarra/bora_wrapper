import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-online",
        action="store_true",
        default=False,
        help="Ejecutar tests que requieren acceso a internet (BORA).",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-online"):
        return
    skip_online = pytest.mark.skip(reason="usar --run-online para ejecutar este test")
    for item in items:
        if "online" in item.keywords:
            item.add_marker(skip_online)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "online: tests que requieren acceso a internet"
    )
