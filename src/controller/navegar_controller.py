from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QThread, QTimer, QEventLoop, Qt
from src.database import DatabaseService
from view.gui.widget_navegar_page import WidgetNavegarPage
from view.gui.empty_widget_navegar_page import EmptyWidgetNavegarPage
from view.gui.progress_widget_nagevar_page import ProgressWidgetNavegarPage

class NavegarController(QThread):
    '''Controller da página de navegação, responsável por apresentar os
    dados inseridos no banco de dados ao usuário'''

    def __init__(self, db:DatabaseService, parent:QWidget, layout:QVBoxLayout):
        QThread.__init__(self)
        self.db = db()
        self.timer = QTimer()
        self.timer.moveToThread(self)
        self.timer.timeout.connect(self.get_coletas)
        self.len_coletas = 0
        self.parent_widget_navegar = parent
        self.layout = layout

    def get_coletas(self) -> None:
        '''Método responsável por coletar os metadados de cada
        coleta'''
        collection_name = self.db['coleta']
        coletas = list(collection_name.find())
        coletas_id = [coleta['_id'].hex for coleta in coletas]
        # Verifica se o widget de página vazia existe
        empty_widget = self.parent_widget_navegar.findChildren(EmptyWidgetNavegarPage)
        if len(coletas)==0:
            if not empty_widget:
                self.layout.addWidget(EmptyWidgetNavegarPage(self.parent_widget_navegar))
        else:
            if empty_widget:
                self.layout.removeWidget(empty_widget[0])
        if len(coletas)>self.len_coletas:
            dif_len = len(coletas)-self.len_coletas
            for coleta in coletas[-dif_len:]:
                self.__insert_widget_navegar(coleta)
            self.len_coletas = len(coletas)
        elif len(coletas)<self.len_coletas:
            for child in self.parent_widget_navegar.findChildren(WidgetNavegarPage):
                if child.uuid_value.text() not in coletas_id:
                    self.layout.removeWidget(child)
            self.len_coletas = len(coletas)

    def insert_progress_widget(self, param) -> None:
        empty_widget = self.parent_widget_navegar.findChildren(EmptyWidgetNavegarPage)
        if empty_widget:
            self.layout.removeWidget(empty_widget[0])
        custom_widget = ProgressWidgetNavegarPage(self.parent_widget_navegar)
        custom_widget.set_uuid(param)
        self.layout.addWidget(custom_widget, 0, Qt.AlignTop)

    def remove_progress_widget(self, param) -> None:
        progress_widget = self.parent_widget_navegar.findChildren(ProgressWidgetNavegarPage)
        for widget in progress_widget:
            if widget.uuid_value.text()==param.hex:
                self.layout.removeWidget(widget)

    def run(self) -> None:
        '''Método responsável por executar a thread da página
        de navegação, atualizando os dados apresentados'''
        self.timer.start(60000)
        loop = QEventLoop()
        loop.exec_()

    def __insert_widget_navegar(self, dados_coleta) -> None:
        '''Método responsável por inserir um novo widget à pagina
        de navegação'''
        custom_widget = WidgetNavegarPage(self.parent_widget_navegar, self.db)
        custom_widget.set_uuid(dados_coleta['_id'])
        custom_widget.set_data(dados_coleta['data'])
        custom_widget.set_api(dados_coleta['apis'])
        custom_widget.set_topicos(dados_coleta['topicos'])
        custom_widget.set_palavras_chaves(dados_coleta['palavras_chaves'])
        custom_widget.signal.update_gui_navegar.connect(self.get_coletas)
        self.layout.addWidget(custom_widget, 0, Qt.AlignTop)
