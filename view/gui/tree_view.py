from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTreeView, QFrame
from PyQt5.QtCore import QSize

from view.gui.standard_item import StandardItem


class QTreeViewCustom(QTreeView):
    '''Classe que implementa a TreeView da página
    de navegação'''

    def __init__(self, parent:QFrame, item_name:str):
        super(QTreeViewCustom, self).__init__(parent)
        self.setHeaderHidden(True)
        #self.setStyleSheet("border:0px black")
        self.expanded.connect(lambda: self.set_minimum_size(100))
        self.collapsed.connect(lambda: self.set_minimum_size(30))
        self.set_Model(item_name)

    def set_Model(self, item_name):
        '''Método para definir o modelo da Tree View'''
        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.items = StandardItem(item_name)
        self.treeModel.appendRow(self.items)
        self.setModel(self.treeModel)
        self.setMinimumSize(QSize(0, 30))
        self.setMaximumSize(QSize(16777215, 200))

    def set_minimum_size(self, size:int):
        '''Método para definir o tamanho mínimo da TreeView'''
        self.setMinimumSize(QSize(0, size))

    def set_items(self, items:list):
        '''Define os items pra cada ramo da árvore'''
        for item in items:
            self.items.appendRow(StandardItem(item))
