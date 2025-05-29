import requests
from requests import Response
from typing import Literal, Callable
import copy

class BORA: 

    BASE_URL = "https://www.boletinoficial.gov.ar"
    DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest"
    }

    def __init__(self, endpoint:str, cookies_session_url:str):
        
        self.endpoint = endpoint
        self.cookies_session_url = cookies_session_url
        self.session = requests.Session()
        self.headers = copy.deepcopy(self.DEFAULT_HEADERS)
        self.headers['Origin'] = self.BASE_URL
        self.headers['Referer'] = self.BASE_URL + self.cookies_session_url
        self.session.headers.update(self.headers)

    def init_session(self): 
        self.session.get(self.BASE_URL + self.cookies_session_url)

    def make_request(self, method:Literal['GET','POST'], data_payload:dict, kwargs:dict)->Response:

        self.init_session()

        if method == "GET": 
            response = self.session.get(self.BASE_URL + self.endpoint, params=data_payload, **kwargs)
            
        elif method == "POST": 
            response = self.session.post(self.BASE_URL + self.endpoint, data=data_payload, **kwargs)
        else: 
            raise(ValueError("'method' must be one of ['GET','POST']"))
        
        response.raise_for_status()

        return response
    
    def parse_response(self, response:Response, response_parser_func:Callable):
        return response_parser_func(response)