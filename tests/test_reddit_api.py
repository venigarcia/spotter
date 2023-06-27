import unittest
from src import RedditAPI
import sys
import os
import warnings

warnings.filterwarnings("ignore")

class TestRedditAPI(unittest.TestCase):
    '''Classe de teste unitário da API do Reddit.'''

    def setUp(self) -> None:
        '''Método responsável por inicializar os dados necessários
        para execução dos testes unitários.'''
        self.USER = os.getenv('API_USER')
        self.PASSWORD = os.environ.get('API_PASSWORD', 'u@QM<r5?MxsUdUD')
        self.KEY = os.getenv('API_KEY')
        self.SECRET_KEY = os.environ.get('API_SECRET_KEY')

    def test_login(self) -> None:
        '''Teste unitário para verificar login na API do Reddit'''
        redditAPI = RedditAPI(self.USER, self.PASSWORD, self.KEY, self.SECRET_KEY)
        self.assertNotEqual(redditAPI.token, None)

    def test_get_topico(self) -> None:
        '''Teste unitário para verificar coleta por tópico
        na API do Reddit'''
        redditAPI = RedditAPI(self.USER, self.PASSWORD, self.KEY, self.SECRET_KEY)
        response = redditAPI.get_posts_with_topics(['python'])
        self.assertNotEqual(response, None)
        self.assertIsInstance(response, list)

    def test_get_palavra_chave(self) -> None:
        '''Teste unitário para verificar coleta por palavra-chave
        na API do Reddit'''
        redditAPI = RedditAPI(self.USER, self.PASSWORD, self.KEY, self.SECRET_KEY)
        response = redditAPI.get_posts_with_key_words(['python'])
        self.assertNotEqual(response, None)
        self.assertIsInstance(response, list)
