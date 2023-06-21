from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QFontDatabase, QColor, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QTableWidgetItem, QAction
import view.resources.resources
#from Custom_Widgets.Widgets import *

class MainWindow(QtWidgets.QMainWindow):
    '''Página principal da aplicação'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("view/gui/main_page.ui", self)
        self.setWindowTitle("Spotter")
        self.Slide_Menu_Num = 0
        self.stackedWidget.setCurrentWidget(self.coletar_page)
        self.menu_slide_btn.clicked.connect(lambda: self.slide_menu())
        self.coletar_btn.clicked.connect(lambda: self.show_coletar_page())
        self.navegar_btn.clicked.connect(lambda: self.show_navegar_page())
        self.historico_btn.clicked.connect(lambda: self.show_historico_page())
        self.info_btn.clicked.connect(lambda: self.show_info_page())
        self.api_btn.clicked.connect(lambda: self.show_api_page())

    def show_coletar_page(self):
        self.stackedWidget.setCurrentWidget(self.coletar_page)

    def show_api_page(self):
        self.stackedWidget.setCurrentWidget(self.api_page)    

    def show_navegar_page(self):
        self.stackedWidget.setCurrentWidget(self.navegar_page)

    def show_historico_page(self):
        self.stackedWidget.setCurrentWidget(self.historico_page)

    def show_info_page(self):
        self.stackedWidget.setCurrentWidget(self.info_page)
    
    def slide_menu(self):
        if self.Slide_Menu_Num==0:
            self.animation1 = QPropertyAnimation(self.left_menu_container, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(200)
            self.animation1.setEndValue(120)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.Slide_Menu_Num = 1
        else:
            self.animation1 = QPropertyAnimation(self.left_menu_container, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(120)
            self.animation1.setEndValue(200)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.Slide_Menu_Num = 0