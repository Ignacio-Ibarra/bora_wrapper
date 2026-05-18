from bs4 import BeautifulSoup
from requests import Response

from bora_wrapper.web.core import BORA


def get_endpoint(seccion: str, id_aviso: str, date: str) -> str:
    return f"/detalleAviso/{seccion}/{id_aviso}/{date}?busqueda=1"


def parse_html_text(response: Response) -> str:
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    return article.get_text(separator="\n", strip=True)


class TextDownloader:
    def __init__(self, seccion: str, id_aviso: str, date: str):
        self.seccion = seccion
        self.id_aviso = id_aviso
        self.date = date
        self.endpoint = get_endpoint(self.seccion, self.id_aviso, self.date)
        self.bora = BORA(endpoint=self.endpoint, cookies_session_url="")

    def get_text(self) -> str:
        response = self.bora.make_request(method="GET", data_payload=None)
        text = self.bora.parse_response(
            response=response, response_parser_func=parse_html_text
        )
        return text
