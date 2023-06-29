'''Classes e métodos exportados:
- RedditAPI'''
from typing import List
from src.interface import ApiInterface
import requests
from uuid import uuid4, UUID
from datetime import datetime


class RedditAPI(ApiInterface):
    '''Classe responsável pela comunicação com a API do
    Reddit'''

    def __init__(self, username:str, password:str, api_key:str,
                 secret_key:str):
        self.__username = username
        self.__password = password
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__name = 'Reddit'
        self.login()

    def set_keys(self, keys: List[str]) -> None:
        '''Método para definir a secret-key da API do
        Reddit'''
        self.__secret_key = keys[0]

    def login(self) -> None:
        '''Método para efetuar login na API do Reddit
        utilizando a secret-key informada'''
        try:
            auth = requests.auth.HTTPBasicAuth(self.__api_key,
                                            self.__secret_key)
            data = {
                'grant_type': 'password',
                'username': self.__username,
                'password': self.__password
            }
            headers = {'User-Agent': 'MyBot/0.0.1'}
            res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers, timeout=200)
            self.token = res.json()['access_token']
        except Exception as error:
            print('Caught this error: ' + repr(error))
            raise error

    def get_name_api(self) -> str:
        '''Método que retorna o nome da api para futura
        identificação'''
        return self.__name

    def get_posts_with_key_words(self, key_words: list) -> list:
        '''Método para coletar comentários do Reddit contendo
        uma ou mais palavras-chaves'''
        try:
            headers = {'User-Agent': 'MyBot/0.0.1'}
            headers = {**headers, **{'Authorization': f"bearer {self.token}"}}
            response = []
            for key_word in key_words:
                url = "https://oauth.reddit.com/search/?q="+key_word+"&include_over_18=1&type=comment"
                res = requests.get(url, params={'limit':'100'}, headers=headers, timeout=200)
                for post in res.json()['data']['children']:
                    id = uuid4()
                    if post['data']['selftext']:
                        data = datetime.fromtimestamp(post['data']['created_utc']).strftime('%d/%m/%y %H:%M')
                        response.append({
                            '_id':id.hex, 
                            'texto': post['data']['selftext'], 
                            'data': data,
                            'api': self.__name,
                            'filtro': key_word,
                            'tipo': 'palavra_chave'})
            return response
        except Exception as error:
            print('Caught this error: ' + repr(error))
            raise error

    def get_posts_with_topics(self, topics: list) -> list:
        '''Método para coletar comentários do Reddit que perteçam
        a um determinado tópico'''
        try:
            headers = {'User-Agent': 'MyBot/0.0.1'}
            headers = {**headers, **{'Authorization': f"bearer {self.token}"}}
            response = []
            for topic in topics:
                url = "https://oauth.reddit.com/api/search_reddit_names/?" \
                        + "exact=0&include_over_18=1&"\
                        +"include_unadvertisable=1&"\
                        +"query="+topic
                res = requests.get(url, params={'limit':'100'}, headers=headers, timeout=200)
                for sub_reddit in res.json()['names']:
                    url = "https://oauth.reddit.com/r/"+ sub_reddit + \
                        "/new/?include_over_18=1&type=comment"
                    res = requests.get(url, params={'limit':'100'}, headers=headers, timeout=200)
                    for post in res.json()['data']['children']:
                        id = uuid4()
                        if post['data']['selftext']:
                            data = datetime.fromtimestamp(post['data']['created_utc']).strftime('%d/%m/%y %H:%M')
                            response.append({
                                '_id':id.hex, 
                                'texto': post['data']['selftext'], 
                                'data': data,
                                'api': self.__name,
                                'filtro': topic,
                                'tipo': 'topico'})
            return response
        except Exception as error:
            print('Caught this error: ' + repr(error))
            raise error
