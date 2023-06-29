from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QFontDatabase, QColor, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QTableWidgetItem, QAction, QMessageBox
import view.resources.resources
from src.controller import ColetarController, NavegarController
from src.database import DatabaseService
from src import RedditAPI
from view.gui.widget_navegar_page import WidgetNavegarPage
import warnings

warnings.filterwarnings("ignore")

class MainWindow(QtWidgets.QMainWindow):
    '''Página principal da aplicação'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("view/gui/main_page.ui", self)
        self.setWindowTitle("Spotter")
        self.navegar_controller = NavegarController(DatabaseService('pfp_base'), 
                                                    self.scrollAreaWidgetContents_2, 
                                                    self.verticalLayout_24)
        self.navegar_controller.start()
        self.navegar_controller.get_coletas()
        self.slide_menu_num = 1
        self.stackedWidget.setCurrentWidget(self.coletar_page)
        self.menu_slide_btn.clicked.connect(lambda: self.slide_menu())
        self.coletar_btn.clicked.connect(lambda: self.show_coletar_page())
        self.navegar_btn.clicked.connect(lambda: self.show_navegar_page())
        self.info_btn.clicked.connect(lambda: self.show_info_page())
        self.api_btn.clicked.connect(lambda: self.show_api_page())
        self.coletar_novos_btn.clicked.connect(lambda: self.coletar_novos_dados())

    def show_coletar_page(self):
        self.stackedWidget.setCurrentWidget(self.coletar_page)

    def show_api_page(self):
        self.stackedWidget.setCurrentWidget(self.api_page)    

    def show_navegar_page(self):
        self.stackedWidget.setCurrentWidget(self.navegar_page)

    def show_info_page(self):
        self.stackedWidget.setCurrentWidget(self.info_page)

    def slide_menu(self):
        if self.slide_menu_num==0:
            self.animation1 = QPropertyAnimation(self.left_menu_container, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(200)
            self.animation1.setEndValue(120)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.slide_menu_num = 1
        else:
            self.animation1 = QPropertyAnimation(self.left_menu_container, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(120)
            self.animation1.setEndValue(200)
            self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation1.start()
            self.slide_menu_num = 0

    def emit_alert_page(self, message) -> None:
        dlg = QMessageBox(self)
        dlg.setWindowTitle("ERROR")
        dlg.setText(message)
        dlg.exec()

    def coletar_novos_dados(self) -> None:
        apis = []
        try:
            if self.radio_btn_reddit.isChecked():
                    self.reddit_api = RedditAPI(self.lineEdit_3.text(), self.lineEdit_4.text(),
                                            self.lineEdit_2.text(), self.lineEdit.text())
                
            apis.append(self.reddit_api)
            if self.radio_btn_topico.isChecked() or self.radio_btn_palavra_chave.isChecked():
                self.coletar_controller = ColetarController(
                                                            DatabaseService('pfp_base'),
                                                            apis,
                                                            self.plainTextEdit_topico.toPlainText(),
                                                            self.plainTextEdit_palavra.toPlainText()
                                                        )
                self.coletar_controller.signal.update_gui_navegar.connect(
                            self.navegar_controller.get_coletas)
                self.coletar_controller.signal.insert_progress_widget.connect(
                            self.navegar_controller.insert_progress_widget
                )
                self.coletar_controller.signal.remove_progress_widget.connect(
                            self.navegar_controller.remove_progress_widget
                )
                self.coletar_controller.signal.error.connect(
                            self.emit_alert_page
                )
                self.coletar_controller.start()
        except Exception:
            self.emit_alert_page("Erro, verifique as chaves inseridas e tente novamente.")

