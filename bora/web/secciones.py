from bora.web.busqueda import BusquedaAvanzadaSeccion
from bora.web.core import BORA
from requests import Response
from bs4 import BeautifulSoup
import json
import copy


class SegundaSeccion(BusquedaAvanzadaSeccion): 
    
    DEFAULT_PARAMS = {
        
            "busquedaRubro": False,
            "hayMasResultadosBusqueda": True,
            "ejecutandoLlamadaAsincronicaBusqueda": False,
            "ultimaSeccion": "",
            "filtroPorRubrosSeccion": False,
            "filtroPorRubroBusqueda": False,
            "filtroPorSeccionBusqueda": False,
            "busquedaOriginal": True,
            "ordenamientoSegunda": False,
            "seccionesOriginales": [2],
            "ultimoItemExterno": None,
            "ultimoItemInterno": None,
            "texto": "",
            "nroNorma": "",
            "anioNorma": "",
            "denominacion": "",
            "tipoContratacion": "",
            "anioContratacion": "",
            "nroContratacion": "",
            "todasLasPalabras": True,
            "comienzaDenominacion": True,
            "tipoBusqueda": "Avanzada",
            "numeroPagina": 1,
            "ultimoRubro": "",
            "seccion" : [2]

        
    }

    def __init__(
            self,
            rubros:list[str]=None,
            fecha_desde:str=None,
            fecha_hasta:str=None
    ):
        
        self.params = copy.deepcopy(self.DEFAULT_PARAMS)
        self.params['rubros'] = rubros
        self.params['fechaDesde'] = fecha_desde
        self.params['fechaHasta'] = fecha_hasta

        self.payload = {
            'params' : json.dumps(self.params),
            "array_volver": "[]"
        }

        @staticmethod
        def parse_response(response: Response):
            html = response.json()['content']['html']
            soup = BeautifulSoup(html, "html.parser")
            return [
                BORA.BASE_URL + a['href']
                for a in soup.find_all('a', class_='puntero') if a.get('href')
            ]
        
        super().__init__(
            seccion='segunda',
            data_payload=self.payload,
            response_parser_func=parse_response,
            request_kwargs=None
        )