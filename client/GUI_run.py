import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from client_base import *
import sys
import GUI_login
import GUI_client

class login_master(GUI_login.Ui_LoginWindow):
    def create_client_connection(self):
        add,port = self.get_address()
        nick = self.lineEdit.text()
        self.client = Client(add,port,nick)
        self.label_2.setText(self.client.error_message)
        if(self.client.connected):
            change_to_main(self.client,MainWindow,add,ui_main)

class main_master(GUI_client.Ui_MainWindow):
    def close_connection(self):
        change_to_login(MainWindow)

def change_to_main(client,MainWindow,server_ip,ui_main):
    ui_main.setup_Ui(MainWindow,client,server_ip)

def change_to_login(MainWindow):
    ui_log.setup_Ui(MainWindow)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui_log = login_master()
ui_main = main_master()
ui_log.setup_Ui(MainWindow)
MainWindow.show()
app.exec_()