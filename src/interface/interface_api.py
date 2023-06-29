'''Classes e métodos exportados:
- ApiInterface'''
import abc
from typing import List


class ApiInterface(metaclass=abc.ABCMeta):
    '''Interface para implementação das API's'''

    @abc.abstractmethod
    def set_keys(self, keys:List[str]) -> None:
        '''Método para definir as keys de acesso
        as API's'''
        raise NotImplementedError

    @abc.abstractmethod
    def login(self) -> None:
        '''Método para efeturar login nas API's'''
        raise NotImplementedError

    @abc.abstractmethod
    def get_posts_with_key_words(self, key_words:list) -> list:
        '''Método para coletar os posts filtrando-os por palavras-chaves'''
        raise NotImplementedError

    @abc.abstractmethod
    def get_posts_with_topics(self, topics:list) -> list:
        '''Método para coletar os posts filtrando-os por tópicos'''
        raise NotImplementedError

    @abc.abstractmethod
    def get_name_api(self) -> str:
        '''Método que retorna o nome da api para futura
        identificação'''
        raise NotImplementedError
