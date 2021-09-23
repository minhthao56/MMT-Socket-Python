
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from services.socket import client, FORMAT


class Ui_AppRunning(object):

    def handleGetListAppRunning(self):
        client.sendall("running-app".encode(FORMAT))
        msg = client.recv(20000).decode(FORMAT)
        listDataTable = json.loads(msg)
        self.tableWidget.setRowCount(listDataTable.__len__())

        if (listDataTable.__len__() > 0):
            for idx, val in enumerate(listDataTable):
                self.tableWidget.setItem(
                    idx, 0, QTableWidgetItem(val["name"]))
                self.tableWidget.setItem(
                    idx, 1, QTableWidgetItem(str(val['id'])))

    def setupUi(self, AppRunning):
        AppRunning.setObjectName("AppRunning")
        AppRunning.resize(533, 600)
        self.centralwidget = QtWidgets.QWidget(AppRunning)
        self.centralwidget.setObjectName("centralwidget")
        # btnKill
        self.btnKill = QtWidgets.QPushButton(self.centralwidget)
        self.btnKill.setGeometry(QtCore.QRect(20, 30, 111, 54))
        self.btnKill.setMaximumSize(QtCore.QSize(320, 54))
        self.btnKill.setObjectName("btnKill")

        # btnXem
        self.btnXem = QtWidgets.QPushButton(self.centralwidget)
        self.btnXem.setGeometry(QtCore.QRect(150, 30, 111, 54))
        self.btnXem.setMaximumSize(QtCore.QSize(320, 54))
        self.btnXem.setObjectName("btnXem")
        self.btnXem.clicked.connect(self.handleGetListAppRunning)

        # btnDelete
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(280, 30, 111, 54))
        self.btnDelete.setMaximumSize(QtCore.QSize(320, 54))
        self.btnDelete.setObjectName("btnDelete")

        # btnStart
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(400, 30, 111, 54))
        self.btnStart.setMaximumSize(QtCore.QSize(320, 54))
        self.btnStart.setObjectName("btnStart")

        # Table
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Name Process", "ID Process"])
        self.tableWidget.setGeometry(20, 100, 490, 490)
        self.tableWidget.verticalHeader().setVisible(False)

        # AppRunning
        AppRunning.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AppRunning)
        self.statusbar.setObjectName("statusbar")
        AppRunning.setStatusBar(self.statusbar)

        self.retranslateUi(AppRunning)
        QtCore.QMetaObject.connectSlotsByName(AppRunning)

    def retranslateUi(self, AppRunning):
        _translate = QtCore.QCoreApplication.translate
        AppRunning.setWindowTitle(_translate("AppRunning", "MainWindow"))
        self.btnKill.setText(_translate("AppRunning", "Kill"))
        self.btnXem.setText(_translate("AppRunning", "Xem"))
        self.btnDelete.setText(_translate("AppRunning", "Xóa"))
        self.btnStart.setText(_translate("AppRunning", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppRunning = QtWidgets.QMainWindow()
    ui = Ui_AppRunning()
    ui.setupUi(AppRunning)
    AppRunning.show()
    sys.exit(app.exec_())
