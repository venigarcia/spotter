'''Classes e métodos exportados:
- RedditAPI'''
from typing import List
from src.interface import ApiInterface


class RedditAPI(ApiInterface):
    '''Classe responsável pela comunicação com a API do
    Reddit'''

    def __init__(self):
        self.secret_key = None

    def set_keys(self, keys: List[str]) -> None:
        '''Método para definir a secret-key da API do
        Reddit'''
        self.secret_key = keys[0]

    def login(self) -> None:
        '''Método para efetuar login na API do Reddit
        utilizando a secret-key informada'''

    def get_posts_with_key_words(self, key_words: List[str]) -> List:
        '''Método para coletar comentários do Reddit contendo
        uma ou mais palavras-chaves'''

    def get_posts_with_topics(self, topics: List[str]) -> List:
        '''Método para coletar comentários do Reddit que perteçam
        a um determinado tópico'''
