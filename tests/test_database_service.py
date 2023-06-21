import unittest
from src.database import DatabaseService


class TestDatabaseService(unittest.TestCase):
    '''Classe de teste unitário do DatabaseService, responsável
    pela conexão e construção do banco de dados.'''

    def setUp(self) -> None:
        '''Método responsável por inicializar os dados necessários
        para execução dos testes unitários.'''
        db = DatabaseService(db_name='post_list_test')
        self.client = db()

    def tearDown(self) -> None:
        '''Método responsável por limpar os dados inseridos durante
        a execução dos testes unitários'''
        collection_name = self.client['post_list_test']
        collection_name.delete_many({})

    def test_collection(self) -> None:
        '''Teste unitário para criação da collection
        do banco de dados.'''
        collection_name = self.client['post_list_test']
        item1 = {
            "_id": "TEST00000001",
            "texto": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        item2 = {
            "_id": "TEST00000002",
            "texto": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        collection_name.insert_many([item1, item2])
        item_details = collection_name.find({"_id" : "TEST00000001"})
        item = item_details[0]
        self.assertEqual(item['_id'], "TEST00000001")
        self.assertEqual(item['texto'], "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
