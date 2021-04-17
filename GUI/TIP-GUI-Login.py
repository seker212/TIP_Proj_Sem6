from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #TextColors
        textColor = "QLabel { color : rgb(100,220,240); }"

        #Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 160)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(20,30,52);")
        MainWindow.setWindowTitle("TIP-Projekt")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Pseudonim
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText("Nickname")
        self.lineEdit.setStyleSheet("background-color : rgb(45,55,82)")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(130,250,250))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(100,220,240))
        self.lineEdit.setPalette(palette)
        self.lineEdit.setObjectName("lineEdit")

        #IP Address
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPlaceholderText("Server IP")
        self.lineEdit_2.setStyleSheet("background-color : rgb(45,55,82)")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(130,250,250))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(100,220,240))
        self.lineEdit_2.setPalette(palette)

        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        port = "(?:[0-5]?[0-9]?[0-9]?[0-9]?[0-9]|6[0-4][0-9][0-9][0-9]|65[0-4][0-9][0-9]|655[0-2][0-9]|6553[0-5])"
        ipRegex = QtCore.QRegExp  ("^" + ipRange
                            + "\\." + ipRange
                            + "\\." + ipRange
                            + "\\." + ipRange
                            + "\\:" + port + "$")
        ipValidator = QtGui.QRegExpValidator(ipRegex)
        self.lineEdit_2.setValidator(ipValidator)

        self.lineEdit_2.setObjectName("lineEdit_2")

        #Join button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color : rgb(45,55,82)")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(100,220,240))
        self.pushButton.setPalette(palette)
        self.pushButton.setObjectName("pushButton")

        #Header
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("Header")
        self.label.setStyleSheet(textColor)
        self.verticalLayout.addWidget(self.label)

        #Error display
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 191, 21))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("Error")
        self.label_2.setStyleSheet("QLabel { color : rgb(240,240,100); }")
        self.verticalLayout_2.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Setup the default
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TIP-Projekt"))
        self.pushButton.setText(_translate("MainWindow", "Join"))
        self.label.setText(_translate("MainWindow", "Join a serwer"))
        self.label_2.setText(_translate("MainWindow", "Error: Nickname already used"))


#Run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
