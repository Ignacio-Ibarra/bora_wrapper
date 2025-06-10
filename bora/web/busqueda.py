from bora.web.core import BORA
from typing import Callable, Optional
from requests import RequestException, Response
import json


def inject_page(page:int, key:str, json_string:str):
    x_dict =  json.loads(json_string)
    x_dict[key] = page
    return json.dumps(x_dict)


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

    def get_result(self, pagina=1, resultados_acumulados=None):
        if resultados_acumulados is None:
            resultados_acumulados = []

        try:
            # Actualizamos el payload con la página actual
            self.data_payload['params'] = inject_page(page=pagina, 
                                                      key='numeroPagina', 
                                                      json_string=self.data_payload['params'])
                       

            response = self.make_request(
                method=self.method,
                data_payload=self.data_payload,
                kwargs=self.request_kwargs
            )

            # Parseamos resultados y los acumulamos
            resultados = self.parse_response(response=response, response_parser_func=self.response_parser_func)
            resultados_acumulados.extend(resultados)

            # Verificamos si hay más páginas
            content = response.json().get("content", {})
            html = content.get("html", "")
            sig_pag = content.get("sig_pag", None)

            if html.strip() != "" and sig_pag:
                return self.get_result(pagina=sig_pag, resultados_acumulados=resultados_acumulados)
            else:
                return resultados_acumulados

        except RequestException as e:
            print(f"[ERROR] Falló la petición en la página {pagina}: {e}")
            return resultados_acumulados

def get_rubros(response:Response):
    return list(map(lambda x: x['name'], response.json()))

class BusquedaRubros(BORA):
    
    def __init__(self,
                 seccion:str,
                 parse_response_func:Callable = get_rubros, 
                 request_kwargs:Optional[dict] = {}):
        
        self.seccion = seccion
        self.method = 'GET'
        self.parse_response_func = parse_response_func
        self.request_kargs = request_kwargs

        super().__init__(
            endpoint=f"/busquedaAvanzada/{self.seccion}/rubros",
            cookies_session_url=f"/busquedaAvanzada/{self.seccion}"
        )

    
    def get_result(self):

        

        try:
            response = self.make_request(method=self.method, 
                                         data_payload=None, 
                                         kwargs=self.request_kargs)

            result = self.parse_response(response=response, 
                                         response_parser_func=self.parse_response_func)
            return result

        except RequestException as e:
            print(f"[ERROR] Falló la petición a la URL {response.url}: {e}")
        except Exception as e: 
            print(f"[ERROR] {e}")

