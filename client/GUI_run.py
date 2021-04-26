import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from client_base import *
import sys
import GUI_login
import GUI_client

class main_master(GUI_login.Ui_LoginWindow):
    def create_client_connection(self):
        add,port = self.get_address()
        nick = self.lineEdit.text()
        self.client = Client(add,port,nick)
        self.label_2.setText(self.client.error_message)
        heheszki(self.client,MainWindow)

def heheszki(client,MainWindow):
    ui_main = GUI_client.Ui_MainWindow()
    ui_main.setup_Ui(MainWindow,client)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui_log = main_master()
ui_log.setup_Ui(MainWindow)
MainWindow.show()
app.exec_()