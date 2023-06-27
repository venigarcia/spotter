import unittest
from src.database import DatabaseService
from view.main_page import MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
import warnings

warnings.filterwarnings("ignore")

class TestMainPage(unittest.TestCase):
    '''Classe de teste unitário da interface da aplicação.'''

    def setUp(self) -> None:
        '''Método responsável por inicializar os dados necessários
        para execução dos testes unitários.'''
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_page = MainWindow()

    def test_labels_coletar_page(self) -> None:
        '''Teste unitário para verificar o conteúdo da página
        de coleta'''
        self.assertEqual(self.main_page.coletar_page_label.text(), 'Coletar novos dados')
        self.assertEqual(self.main_page.label_topico.text(), 'Tópicos')
        self.assertEqual(self.main_page.label_palavra_chave.text(), 'Palavras-chaves')
        self.assertEqual(self.main_page.radio_btn_topico.text(), 'Incluir tópicos')
        self.assertEqual(self.main_page.radio_btn_palavra_chave.text(), 'Incluir palavras-chaves')

    def test_labels_api_page(self) -> None:
        '''Teste unitário para verificar o conteúdo da página
        de APIs'''
        self.assertEqual(self.main_page.api_page_label.text(), 'APIs')
        self.assertEqual(self.main_page.label_6.text(), 'Usuário')
        self.assertEqual(self.main_page.label_7.text(), 'Senha  ')
        self.assertEqual(self.main_page.label_4.text(), 'API Key    ')
        self.assertEqual(self.main_page.label_5.text(), 'Secret Key')
        self.assertEqual(self.main_page.label_logo_reddit_2.text(), 'Reddit')

    def test_slide_menu(self) -> None:
        '''Teste unitário para verificar a expansão do menu lateral'''
        QTest.mouseClick(self.main_page.menu_slide_btn, Qt.LeftButton)
        self.assertEqual(self.main_page.left_menu_container.maximumWidth(), 120)
        QTest.mouseClick(self.main_page.menu_slide_btn, Qt.LeftButton)
        self.assertEqual(self.main_page.left_menu_container.maximumWidth(), 200)

    def test_slide_menu_click_coleta(self) -> None:
        '''Teste unitário para verificar a expansão do menu lateral'''
        QTest.mouseClick(self.main_page.coletar_btn, Qt.LeftButton)
        self.assertEqual(self.main_page.stackedWidget.currentWidget(), self.main_page.coletar_page)
    
    def test_slide_menu_click_navegar(self) -> None:
        '''Teste unitário para verificar a expansão do menu lateral'''
        QTest.mouseClick(self.main_page.navegar_btn, Qt.LeftButton)
        self.assertEqual(self.main_page.stackedWidget.currentWidget(), self.main_page.navegar_page)
    
    def test_slide_menu_click_api(self) -> None:
        '''Teste unitário para verificar a expansão do menu lateral'''
        QTest.mouseClick(self.main_page.api_btn, Qt.LeftButton)
        self.assertEqual(self.main_page.stackedWidget.currentWidget(), self.main_page.api_page)
    
    def test_slide_menu_click_info(self) -> None:
        '''Teste unitário para verificar a expansão do menu lateral'''
        QTest.mouseClick(self.main_page.info_btn, Qt.LeftButton)
        self.assertEqual(self.main_page.stackedWidget.currentWidget(), self.main_page.info_page)