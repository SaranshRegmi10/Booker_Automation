import requests
from config.settings import settings

class BaseClient:
    def __init__(self,base_url:str = settings.BASE_URL):
        self.base_url = base_url
        self.session = requests.session()
        self.session.headers.update(
            {
                "Content-Type":"application/json",
                "Accept" : "application/json"
            }
        )
    def _full_url(self,endpoint:str) -> str:
        return f"{self.base_url.rstrip("/")}/{endpoint.lstrip("/")}"

    def get(self,endpoint:str, params: dict =None, headers:dict = None):
        url = self._full_url(endpoint)
        return self.session.get(url,params=params,headers=headers, timeout= 10)
    
    def post(self, endpoint: str, data: dict = None, headers: dict = None):
        url = self._full_url(endpoint)
        return self.session.post(url, json=data, headers=headers, timeout=10)
    
    def put(self,endpoint:str, data:dict = None, headers: dict = None):
        url = self._full_url(endpoint)
        return self.session.put(url,json=data,headers=headers,timeout=10)

    def delete(self,endpoint:str,headers:dict=None):
        url = self._full_url(endpoint)
        return self.session.delete(url,headers=headers,timeout=10)