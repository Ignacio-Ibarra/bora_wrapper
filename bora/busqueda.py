from bora.core import BORA
from typing import Callable
from requests import RequestException

class BusquedaAvanzadaSeccion(BORA):
    def __init__(
        self,
        seccion: str,
        data_payload: dict = None,
        response_parser_func: Callable = None,
        request_kwargs: dict = None
    ):
        self.seccion = seccion
        self.method = "POST"
        self.data_payload = data_payload or {}
        self.response_parser_func = response_parser_func
        self.request_kwargs = request_kwargs or {}

        super().__init__(
            endpoint=f"/busquedaAvanzada/realizarBusqueda/{self.seccion}",
            cookies_session_url=f"/busquedaAvanzada/{self.seccion}"
        )

    def get_result(self):
        try:
            response = self.make_request(
                method=self.method,
                data_payload=self.data_payload,
                kwargs=self.request_kwargs
            )
            return self.parse_response(response=response, response_parser_func=self.response_parser_func)
        except RequestException as e:
            print(f"[ERROR] Falló la petición: {e}")
            return []