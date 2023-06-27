from PyQt5.QtGui import (QStandardItem, QColor, QFont)


class StandardItem(QStandardItem):
    '''Classe que implementa os itens da TreeView da página
    de navegação'''

    def __init__(self, text='', color=QColor(255, 255, 255)):
        super().__init__()
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.setEditable(False)
        self.setForeground(QColor(255, 255, 255))
        self.setFont(font)
        self.setText(text)
