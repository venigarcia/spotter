from PyQt5.QtCore import QThread, pyqtSignal, QObject
from typing import List
from src.interface import ApiInterface
from uuid import uuid4, UUID
from src.database import DatabaseService
from datetime import datetime


class ColetarController(QThread):
    '''Controller da página de coleta, responsável por executar as chamadas
    às APIs e armazenar os dados encontrados no bando de dados'''

    def __init__(self, db:DatabaseService, apis: List[ApiInterface], topicos:str=None,
                             palavras_chaves:str=None):
        QThread.__init__(self)
        self.db = db()
        self.apis = apis
        self.topicos = topicos
        self.palavras_chaves = palavras_chaves
        self.signal = Signals()

    def run(self) -> None:
        '''Método responsável por realizar chamadas às APIs e organizar a resposta
        em um dicionário'''
        try:
            id_coleta = uuid4()
            #Dicionário que irá armazenar os resultados das chamadas às APIs
            dict_response = {}
            #Lista com os nomes das APIs utilizadas
            list_apis_names = []
            #Data da coleta
            data = datetime.now()
            for api in self.apis:
                dict_response.update({
                    api.get_name_api(): []
                })
                list_apis_names.append(api.get_name_api())
                if self.palavras_chaves:
                    res = api.get_posts_with_key_words(self.palavras_chaves.split(';'))
                    dict_response[api.get_name_api()] = dict_response[api.get_name_api()] + res
                if self.topicos:
                    res = api.get_posts_with_topics(self.topicos.split(';'))
                    dict_response[api.get_name_api()] = dict_response[api.get_name_api()] + res
            self.__inserir_dados_sentencas(dict_response, id_coleta)
            self.__inserir_dados_coleta(list_apis_names, id_coleta,
                                    self.topicos, self.palavras_chaves, data)
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def __inserir_dados_sentencas(self, dict_response:dict, id_coleta:UUID) -> None:
        '''Insere os dados coletados através das chamadas às APIS
        no banco de dados'''
        try:
            collection_name = self.db['sentencas']
            for key in dict_response.keys():
                for dado in dict_response[key]:
                    dado['id_coleta'] = id_coleta.hex
                collection_name.insert_many(dict_response[key])
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def __inserir_dados_coleta(self, list_apis_names:list, id_coleta:UUID,
                             topicos:list, palavras_chaves:list, data: datetime) -> None:
        '''Insere os metadados utilizados para executar a coleta no 
        banco de dados. Exemplo de metadados são, APIs utilizadas, os tópicos,
        palavras-chaves, data de execução. etc'''
        try:
            collection_name = self.db['coleta']
            coleta = {
                '_id': id_coleta,
                'data': data,
                'apis': ', '.join(list_apis_names),
                'topicos': ', '.join(topicos.split(';')) if topicos else None,
                'palavras_chaves': ', '.join(palavras_chaves.split(';')) \
                                        if palavras_chaves else None
            }
            collection_name.insert_one(coleta)
            self.signal.update_gui_navegar.emit()
        except Exception as error:
            print('Caught this error: ' + repr(error))

class Signals(QObject):
    '''Classe para emissão de sinais entre os controllers'''
    update_gui_navegar = pyqtSignal()
