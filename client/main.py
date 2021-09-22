
from PyQt5 import QtCore, QtWidgets
import socket

PORT = 65432
FORMAT = "utf8"
# Socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Ui_MainApp(object):

    def handleConnectServer(self):
        SERVER = self.inputIP.text()
        try:
            client.connect((SERVER, PORT))
            print("Kết nối thành công!!!")
            client.sendall("check".encode(FORMAT))
            msg = client.recv(1024).decode(FORMAT)
            print(msg)
            if (msg == "connected"):
                self.showPopup()

        except:
            print("ERROR SOCKET")

    def handleGetListAppRunning(self):
        client.sendall("running-app".encode(FORMAT))
        msg = client.recv(1024).decode(FORMAT)
        print(msg)

    def setupUi(self, MainApp):
        MainApp.setObjectName("MainApp")
        MainApp.resize(543, 600)
        self.centralwidget = QtWidgets.QWidget(MainApp)
        self.centralwidget.setObjectName("centralwidget")
        # btnConnect
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(370, 50, 151, 51))
        self.btnConnect.setObjectName("btnConnect")
        self.btnConnect.clicked.connect(self.handleConnectServer)
        # inputIP
        self.inputIP = QtWidgets.QLineEdit(self.centralwidget)
        self.inputIP.setGeometry(QtCore.QRect(29, 50, 311, 50))
        self.inputIP.setMinimumSize(QtCore.QSize(0, 0))
        self.inputIP.setMaximumSize(QtCore.QSize(320, 54))
        self.inputIP.setText("")
        self.inputIP.setObjectName("inputIP")
        # btnProcessRunning
        self.btnProcessRunning = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcessRunning.setGeometry(QtCore.QRect(30, 140, 141, 381))
        self.btnProcessRunning.setObjectName("btnProcessRunning")
        # btnAppRunning
        self.btnAppRunning = QtWidgets.QPushButton(self.centralwidget)
        self.btnAppRunning.setGeometry(QtCore.QRect(180, 140, 191, 101))
        self.btnAppRunning.setObjectName("btnAppRunning")
        self.btnAppRunning.clicked.connect(self.handleGetListAppRunning)
        # btnShutDown
        self.btnShutDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnShutDown.setGeometry(QtCore.QRect(180, 260, 61, 121))
        self.btnShutDown.setObjectName("btnShutDown")
        # btnCapScreen
        self.btnCapScreen = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapScreen.setGeometry(QtCore.QRect(250, 260, 121, 121))
        self.btnCapScreen.setObjectName("btnCapScreen")
        # btnEditRegistry
        self.btnEditRegistry = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditRegistry.setGeometry(QtCore.QRect(180, 400, 261, 121))
        self.btnEditRegistry.setObjectName("btnEditRegistry")
        # btnSkystoke
        self.btnSkystoke = QtWidgets.QPushButton(self.centralwidget)
        self.btnSkystoke.setGeometry(QtCore.QRect(380, 140, 151, 241))
        self.btnSkystoke.setObjectName("btnSkystoke")
        # btnExit
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(450, 400, 75, 121))
        self.btnExit.setObjectName("btnExit")

        # MainApp
        MainApp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainApp)
        self.statusbar.setObjectName("statusbar")
        MainApp.setStatusBar(self.statusbar)

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "MainWindow"))
        self.btnConnect.setText(_translate("MainApp", "Kết nối"))
        self.btnProcessRunning.setText(_translate("MainApp", "Process Runing"))
        self.btnAppRunning.setText(_translate("MainApp", "App running"))
        self.btnShutDown.setText(_translate("MainApp", "Tắt\nmáy"))
        self.btnCapScreen.setText(_translate("MainApp", "Chụp màn\nhình"))
        self.btnEditRegistry.setText(_translate("MainApp", "Sửa registry"))
        self.btnSkystoke.setText(_translate("MainApp", "Skeystoke"))
        self.btnExit.setText(_translate("MainApp", "Thoát"))

    def showPopup(self):
        mgs = QtWidgets.QMessageBox()
        mgs.setWindowTitle("Kết nối thành công")
        mgs.setText("Kết nối server thành công")
        mgs.setIcon(QtWidgets.QMessageBox.Icon.Information)
        mgs.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApp = QtWidgets.QMainWindow()
    ui = Ui_MainApp()
    ui.setupUi(MainApp)
    MainApp.show()
    sys.exit(app.exec_())
