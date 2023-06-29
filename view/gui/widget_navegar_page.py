from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QFrame, QHBoxLayout, 
                             QLabel, QTreeView, QSizePolicy)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pymongo import MongoClient
from view.gui.tree_view import QTreeViewCustom
from uuid import UUID
from datetime import datetime


class WidgetNavegarPage(QWidget):
    '''Classe que implementa o widget da página de navegação
    que contém as informações dos dados coletados'''

    def __init__(self, parent:QWidget, db:MongoClient):
        super(WidgetNavegarPage, self).__init__(parent)
        self.signal = Signals()
        self.db = db
        # Fonte do Widget
        self.fonte = QFont()
        self.fonte.setPointSize(10)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.setObjectName("widget_navegar_page_"+str(index))
        #print(self.objectName())
        #self.setStyleSheet(style)

        self.verticalLayout = QVBoxLayout(self)

        # Frame do WidgetNavegarPage
        self.frame = QFrame(self)
        self.frame.setStyleSheet("border: 1px solid #0074E4; border-radius:3px")

        # Vertical layout do WidgetNavegarPage
        self.verticalLayout_1 = QVBoxLayout(self.frame)

        #Frame UUID e Data
        self.frame_1 = QFrame(self.frame)
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.frame_1.setStyleSheet("border: 0px")

        # HorizontalLayout do frame de UUID e Data
        self.horizontalLayout_1 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_1.setContentsMargins(-1, 0, -1, 0)

        # Frame UUID
        self.frame_2 = QFrame(self.frame_1)
        self.frame_2.setFont(self.fonte)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setStyleSheet("border:0px")

        # HorizontalLayout do frame de UUID
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)

        # UUID Label
        uuid_label = QLabel(self.frame_2)
        uuid_label.setFont(self.fonte)
        uuid_label.setText("UUID: ")
        uuid_label.setStyleSheet("border:0px")
        self.horizontalLayout_2.addWidget(uuid_label)

        # Valor da UUID
        self.uuid_value = QLabel(self.frame_2)
        self.uuid_value.setFont(self.fonte)
        self.uuid_value.setStyleSheet("border:0px;background-color:#0BE3D9;padding:5px 10px")
        self.horizontalLayout_2.addWidget(self.uuid_value)

        # Adicionando o frame de UUID ao layout do frame de UUID e Data
        self.horizontalLayout_1.addWidget(self.frame_2, 0, Qt.AlignTop)

        # Frame Data
        self.frame_3 = QFrame(self.frame_1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setStyleSheet("border:0px")

        # HorizontalLayout do frame de Data
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)

        # Data Label
        data_label = QLabel(self.frame_3)
        data_label.setObjectName(u"data_label")
        data_label.setFont(self.fonte)
        data_label.setText("Data: ")
        data_label.setStyleSheet("border:0px")
        self.horizontalLayout_3.addWidget(data_label)

        # Valor da Data
        self.data_value = QLabel(self.frame_3)
        self.data_value.setFont(self.fonte)
        self.data_value.setStyleSheet("border:0px")
        self.horizontalLayout_3.addWidget(self.data_value)

        # Adicionado o frame de data ao layour do frame de UUID e Data
        self.horizontalLayout_1.addWidget(self.frame_3, 0, Qt.AlignTop)

        # Lixeira
        self.lixeira = QPushButton(self.frame_1)
        self.lixeira.setObjectName(u"lixeira")
        self.lixeira.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/Trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lixeira.setIcon(icon7)
        self.lixeira.setIconSize(QSize(25, 25))
        self.lixeira.setStyleSheet("QPushButton{background-color:#0074E4;text-align: center;}"\
                                   "QPushButton:hover{background-color:#0C49FA;color: white;}"\
                                   "QPushButton:hover:pressed {background-color:#0E0CF0;}")
        self.lixeira.clicked.connect(self.remover_coleta)
        self.horizontalLayout_1.addWidget(self.lixeira, 0, Qt.AlignRight|Qt.AlignTop)

        # Adicionando o frame de UUID e Data ao layout do WidgetNavegarPage
        self.verticalLayout_1.addWidget(self.frame_1, 0, Qt.AlignTop)

        # Frame da API
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setStyleSheet("border:0px")

        # HorizontalLayout do frame da API
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)

        # Frame API Label
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setStyleSheet("border:0px")

        # HorizontalLayout do frame da API Label
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)


        # API Label
        api_label = QLabel(self.frame_5)
        api_label.setFont(self.fonte)
        api_label.setText("APIs: ")
        api_label.setStyleSheet("border:0px")
        self.horizontalLayout_5.addWidget(api_label)

        # Adicionando o frame da API Label ao layout do frame da API
        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)

        # Frame do Valor da API
        self.frame_6 = QFrame(self.frame_4)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setStyleSheet("border:0px")

        # HorizontalLayout do frame da API Label
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)

        # Valor API
        self.api_value = QLabel(self.frame_6)
        self.api_value.setFont(self.fonte)
        self.api_value.setStyleSheet("border:0px")
        self.horizontalLayout_6.addWidget(self.api_value)

        # Adicionando o frame do Valor API ao layout do frame da API
        self.horizontalLayout_4.addWidget(self.frame_6)

        # Adicionando o frame da API ao layout do frame do WidgetNavegarPage
        self.verticalLayout_1.addWidget(self.frame_4)

        # Frame do topico
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setStyleSheet("border:0px")

        # HorizontalLayout do topico
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)

        # TreeView do Topico
        self.treeView = QTreeViewCustom(self.frame_7, 'Tópicos')
        self.horizontalLayout_7.addWidget(self.treeView, 0, Qt.AlignTop)

        #Adicionando o frame do topico ao layout do WidgetNavegarPage
        self.verticalLayout_1.addWidget(self.frame_7, 0, Qt.AlignTop)

        #Frame das Palavras-chaves
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setStyleSheet("border:0px")

        # HorizontalLayout das Palavras-chaves
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)

        # TreeView das Palavras-chaves
        self.treeView_2 = QTreeViewCustom(self.frame_8, 'Palavras-chave')
        self.horizontalLayout_8.addWidget(self.treeView_2, 0, Qt.AlignTop)

        # Adicionando o frame das palavras-chaves ao layout do WidgetNavegarPage
        self.verticalLayout_1.addWidget(self.frame_8)

        self.verticalLayout.addWidget(self.frame)

    def set_data(self, data:datetime):
        '''Método responsável por definir o valor da data no
        WidgetNagevarPage'''
        self.data_value.setText(data.strftime("%d/%m/%Y, %H:%M:%S"))

    def set_uuid(self, uuid:UUID):
        '''Método responsável por definir o valor do UUID no
        WidgetNagevarPage'''
        self.uuid = uuid
        self.uuid_value.setText(uuid.hex)

    def set_api(self, apis:str):
        '''Método responsável por definir o valor da api no
        WidgetNagevarPage'''
        self.api_value.setText(apis)

    def set_topicos(self, items:str) -> None:
        '''Método responsável por definir o valor dos tópicos no
        WidgetNagevarPage'''
        if items is not None:
            self.treeView.set_items(items.split(','))

    def set_palavras_chaves(self, items:str) -> None:
        '''Método responsável por definir o valor das palavras-chaves no
        WidgetNagevarPage'''
        if items is not None:
            self.treeView_2.set_items(items.split(','))

    def remover_coleta(self):
        '''Método responsável por remover os dados de coleta e
        as sentenças a partir da id da coleta'''
        collection_name = self.db['sentencas']
        collection_name.delete_many({'id_coleta':self.uuid_value.text()})
        collection_name = self.db['coleta']
        collection_name.delete_one({'_id':self.uuid})
        self.signal.update_gui_navegar.emit()

class Signals(QObject):
    '''Classe para emissão de sinais entre os controllers'''
    update_gui_navegar = pyqtSignal()
