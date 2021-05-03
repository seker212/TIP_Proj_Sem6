from PyQt5 import QtCore, QtGui, QtWidgets
from client_base import *
from abc import ABC, abstractmethod
import threading, time


class Ui_MainWindow(ABC):
    def setup_Ui(self, MainWindow, client):
        
        self.client = client

        #TextColors
        textColor = "QLabel { color : rgb(100,220,240); }"
        
        #Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250,400)
        MainWindow.setFixedSize(250, 400)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(20,30,52);")
        MainWindow.setWindowTitle("TIP-Projekt")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Logout button
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(180, 360, 61, 31))
        self.logout_button.setStyleSheet("background-color : rgb(45,55,82)")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(100,220,240))
        self.logout_button.setPalette(palette)
        self.logout_button.setObjectName("logout_button")
        self.logout_button.clicked.connect(self.close_connection)

        #Top line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 340, 231, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #Users pseudonim
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 360, 111, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.pseudonim_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.pseudonim_layout.setContentsMargins(0, 0, 0, 0)
        self.pseudonim_layout.setObjectName("pseudonim_layout")
        self.pseudonim_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pseudonim_label.setFont(font)
        self.pseudonim_label.setTextFormat(QtCore.Qt.PlainText)
        self.pseudonim_label.setScaledContents(False)
        self.pseudonim_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pseudonim_label.setObjectName("pseudonim_label")
        self.pseudonim_label.setStyleSheet(textColor)
        self.pseudonim_layout.addWidget(self.pseudonim_label)
        self.pseudonim_label.setText(self.client.nick)

        #Bottom line
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 30, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #Main header with server ip
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.server_address_text_label = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.server_address_text_label.setContentsMargins(0, 0, 0, 0)
        self.server_address_text_label.setObjectName("server_address_text_label")
        self.server_address_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.server_address_label.setFont(font)
        self.server_address_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.server_address_label.setLineWidth(0)
        self.server_address_label.setTextFormat(QtCore.Qt.PlainText)
        self.server_address_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_address_label.setObjectName("server_address_label")
        self.server_address_label.setStyleSheet(textColor)
        self.server_address_text_label.addWidget(self.server_address_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 10, 101, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.ip_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ip_layout.setContentsMargins(0, 0, 0, 0)
        self.ip_layout.setObjectName("ip_layout")
        self.ip_address_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ip_address_label.setFont(font)
        self.ip_address_label.setTextFormat(QtCore.Qt.PlainText)
        self.ip_address_label.setObjectName("ip_address_label")
        self.ip_address_label.setStyleSheet(textColor)
        self.ip_address_label.setText(self.client.target_ip)
        self.ip_layout.addWidget(self.ip_address_label)

        #Radiobutton
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 360, 51, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.mute_box_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.mute_box_layout.setContentsMargins(0, 0, 0, 0)
        self.mute_box_layout.setObjectName("mute_box_layout")
        self.mute_box = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.mute_box.setFont(font)
        self.mute_box.setObjectName("mute_box")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(100,220,240))
        self.mute_box.setPalette(palette)
        self.mute_box_layout.addWidget(self.mute_box)

        #Header
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 50, 181, 21))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.participants_title_layput = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.participants_title_layput.setContentsMargins(0, 0, 0, 0)
        self.participants_title_layput.setObjectName("participants_title_layput")
        self.participants_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.participants_label.setTextFormat(QtCore.Qt.PlainText)
        self.participants_label.setAlignment(QtCore.Qt.AlignCenter)
        self.participants_label.setObjectName("participants_label")
        self.participants_label.setStyleSheet(textColor)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.participants_label.setFont(font)
        self.participants_title_layput.addWidget(self.participants_label)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(190, 50, 51, 21))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.participants_total_number_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.participants_total_number_layout.setContentsMargins(0, 0, 0, 0)
        self.participants_total_number_layout.setObjectName("participants_total_number_layout")
        self.participants_number = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.participants_number.setTextFormat(QtCore.Qt.PlainText)
        self.participants_number.setAlignment(QtCore.Qt.AlignCenter)
        self.participants_number.setObjectName("participants_number")
        self.participants_number.setStyleSheet(textColor)
        self.participants_total_number_layout.addWidget(self.participants_number)
        
        #Participant numbers
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 80, 21, 261))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.participant_numbers_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.participant_numbers_layout.setContentsMargins(0, 0, 0, 0)
        self.participant_numbers_layout.setObjectName("participant_numbers_layout")
        
        self.number_label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_1.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_1.setObjectName("number_label_1")
        self.number_label_1.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_1)
        self.number_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_2.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_2.setObjectName("number_label_2")
        self.number_label_2.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_2)
        self.number_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_3.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_3.setObjectName("number_label_3")
        self.number_label_3.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_3)
        self.number_label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_4.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_4.setObjectName("number_label_4")
        self.number_label_4.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_4)
        self.number_label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_5.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_5.setObjectName("number_label_5")
        self.number_label_5.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_5)
        self.number_label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_6.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_6.setObjectName("number_label_6")
        self.number_label_6.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_6)
        self.number_label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_7.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_7.setObjectName("number_label_7")
        self.number_label_7.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_7)
        self.number_label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_8.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_8.setObjectName("number_label_8")
        self.number_label_8.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_8)
        self.number_label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.number_label_9.setTextFormat(QtCore.Qt.PlainText)
        self.number_label_9.setObjectName("number_label_9")
        self.number_label_9.setStyleSheet(textColor)
        self.participant_numbers_layout.addWidget(self.number_label_9)

        #Participant names
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(40, 80, 201, 261))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.participants_list_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.participants_list_layout.setContentsMargins(0, 0, 0, 0)
        self.participants_list_layout.setObjectName("participants_list_layout")

        self.participant1 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant1.setTextFormat(QtCore.Qt.PlainText)
        self.participant1.setObjectName("participant1")
        self.participant1.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant1)
        self.participant2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant2.setTextFormat(QtCore.Qt.PlainText)
        self.participant2.setObjectName("participant2")
        self.participant2.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant2)
        self.participant3 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant3.setTextFormat(QtCore.Qt.PlainText)
        self.participant3.setObjectName("participant3")
        self.participant3.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant3)
        self.participant4 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant4.setTextFormat(QtCore.Qt.PlainText)
        self.participant4.setObjectName("participant4")
        self.participant4.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant4)
        self.participant5 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant5.setTextFormat(QtCore.Qt.PlainText)
        self.participant5.setObjectName("participant5")
        self.participant5.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant5)
        self.participant6 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant6.setTextFormat(QtCore.Qt.PlainText)
        self.participant6.setObjectName("participant6")
        self.participant6.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant6)
        self.participant7 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant7.setTextFormat(QtCore.Qt.PlainText)
        self.participant7.setObjectName("participant7")
        self.participant7.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant7)
        self.participant8 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant8.setTextFormat(QtCore.Qt.PlainText)
        self.participant8.setObjectName("participant8")
        self.participant8.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant8)
        self.participant9 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.participant9.setTextFormat(QtCore.Qt.PlainText)
        self.participant9.setObjectName("participant9")
        self.participant9.setStyleSheet(textColor)
        self.participants_list_layout.addWidget(self.participant9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thread = Update_Thread()
        self.thread.start()
        self.thread.start_signal.connect(self.update_participants)

#Setup the default
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.logout_button.setText(_translate("MainWindow", "Logout"))
        self.server_address_label.setText(_translate("MainWindow", "Server IP Address: "))
        self.participants_label.setText(_translate("MainWindow", "            Participants"))
        self.participants_number.setText(_translate("MainWindow", "1"))
        self.mute_box.setText(_translate("MainWindow", "Mute"))
        self.number_label_1.setText(_translate("MainWindow", "1."))
        self.number_label_2.setText(_translate("MainWindow", "2."))
        self.number_label_3.setText(_translate("MainWindow", "3."))
        self.number_label_4.setText(_translate("MainWindow", "4."))
        self.number_label_5.setText(_translate("MainWindow", "5."))
        self.number_label_6.setText(_translate("MainWindow", "6."))
        self.number_label_7.setText(_translate("MainWindow", "7."))
        self.number_label_8.setText(_translate("MainWindow", "8."))
        self.number_label_9.setText(_translate("MainWindow", "9."))
        self.participant1.setText(_translate("MainWindow", " "))
        self.participant2.setText(_translate("MainWindow", " "))
        self.participant3.setText(_translate("MainWindow", " "))
        self.participant4.setText(_translate("MainWindow", " "))
        self.participant5.setText(_translate("MainWindow", " "))
        self.participant6.setText(_translate("MainWindow", " "))
        self.participant7.setText(_translate("MainWindow", " "))
        self.participant8.setText(_translate("MainWindow", " "))
        self.participant9.setText(_translate("MainWindow", " "))

    def update_participants(self):
        self.participants_number.setText(str(len(self.client.other_participants)+1))
        if(len(self.client.other_participants)>0):
            self.participant1.setText(self.client.other_participants[0])
        if(len(self.client.other_participants)>1):
            self.participant2.setText(self.client.other_participants[1])
        if(len(self.client.other_participants)>2):
            self.participant3.setText(self.client.other_participants[2])
        if(len(self.client.other_participants)>3):
            self.participant4.setText(self.client.other_participants[3])
        if(len(self.client.other_participants)>4):
            self.participant5.setText(self.client.other_participants[4])
        if(len(self.client.other_participants)>5):
            self.participant6.setText(self.client.other_participants[5])
        if(len(self.client.other_participants)>6):
            self.participant7.setText(self.client.other_participants[6])
        if(len(self.client.other_participants)>7):
            self.participant8.setText(self.client.other_participants[7])
        if(len(self.client.other_participants)>8):
            self.participant9.setText(self.client.other_participants[8])

#Close connection method placeholder
    @abstractmethod
    def close_connection(self):
        pass

class Update_Thread(QtCore.QThread):

    start_signal = QtCore.pyqtSignal(bool)

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        while True:
            time.sleep(0.5)
            self.start_signal.emit(True)



#Run
#def run_mainWindow(client):
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setup_Ui(MainWindow,client)
#    MainWindow.show()
