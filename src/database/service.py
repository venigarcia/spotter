'''Classes e métodos exportados:
- DatabaseService'''
from pymongo import MongoClient


class DatabaseService():
    '''Classe responsável pela construção e comunicação
    com o banco de dados.'''
    def __init__(self, db_name:str, db_host:str='localhost', db_port:int=27017):
        self.db_name = db_name
        self.db_host = db_host
        self.db_port = db_port

    def __call__(self):
        return self.__get_database()[self.db_name]

    def __get_database(self):
        '''Método responsável por criar uma conexão com o
        banco de dados'''
        client = MongoClient(host=self.db_host, port=self.db_port, uuidRepresentation='standard')
        return client
