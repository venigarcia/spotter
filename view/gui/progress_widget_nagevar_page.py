from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QFrame, QHBoxLayout, 
                             QLabel, QTreeView, QSizePolicy)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pymongo import MongoClient
from view.gui.tree_view import QTreeViewCustom
from uuid import UUID
from datetime import datetime

class ProgressWidgetNavegarPage(QWidget):
    def __init__(self, parent:QWidget):
        super(ProgressWidgetNavegarPage, self).__init__(parent)
        self.fonte = QFont()
        self.fonte.setPointSize(10)
        self.verticalLayout = QVBoxLayout(self)
        # Frame do ProgressWidgetNavegarPage
        self.frame = QFrame(self)
        self.frame.setStyleSheet("border: 1px solid #0074E4; border-radius:3px")
        self.setStyleSheet(u"border: 1px solid #0074E4; border-radius:3px")
        self.horizontalLayout_27 = QHBoxLayout(self.frame)
        self.frame_uuid = QFrame(self.frame)
        self.frame_uuid.setFont(self.fonte)
        self.frame_uuid.setStyleSheet(u"border: 0px;")
        self.frame_uuid.setFrameShape(QFrame.StyledPanel)
        self.frame_uuid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_uuid)
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.uuid_label = QLabel(self.frame_uuid)
        self.uuid_label.setFont(self.fonte)
        self.uuid_label.setText("UUID: ")

        self.horizontalLayout_28.addWidget(self.uuid_label)

        self.uuid_value = QLabel(self.frame_uuid)
        self.uuid_value.setFont(self.fonte)
        self.uuid_value.setStyleSheet(u"border:0px;background-color:#0BE3D9;padding:1px 10px")

        self.horizontalLayout_28.addWidget(self.uuid_value)


        self.horizontalLayout_27.addWidget(self.frame_uuid, 0, Qt.AlignLeft)

        self.frame_busca = QFrame(self.frame)
        self.frame_busca.setFont(self.fonte)
        self.frame_busca.setStyleSheet(u"border:0px;")
        self.frame_busca.setFrameShape(QFrame.StyledPanel)
        self.frame_busca.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_busca)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.busca_label = QLabel(self.frame_busca)
        self.busca_label.setFont(self.fonte)
        self.busca_label.setText("Buscando...")
        self.busca_label.setStyleSheet(u"border:0px;background-color:#0BE3D9;padding:5px 10px")

        self.horizontalLayout_29.addWidget(self.busca_label)


        self.horizontalLayout_27.addWidget(self.frame_busca, 0, Qt.AlignRight)

        self.verticalLayout.addWidget(self.frame)

    def set_uuid(self, uuid:UUID) -> None:
        '''Método responsável por definir o valor do UUID no
        ProgressWidgetNavegarPage'''
        self.uuid_value.setText(uuid.hex)
