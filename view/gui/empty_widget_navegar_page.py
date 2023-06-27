from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QFrame, QHBoxLayout, 
                             QLabel, QTreeView, QSizePolicy)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class EmptyWidgetNavegarPage(QWidget):
    '''Classe que implementa o widget da página de navegação
    vazia'''

    def __init__(self, parent:QWidget):
        super(EmptyWidgetNavegarPage, self).__init__(parent)
        self.verticalLayout = QVBoxLayout(self)
        self.label_navegar_dados = QLabel(self)
        self.label_navegar_dados.setObjectName(u"label_navegar_dados")
        self.verticalLayout.addWidget(self.label_navegar_dados, 0, Qt.AlignHCenter)
        self.label_navegar_dados.setText("Não possui dados coletados.")
