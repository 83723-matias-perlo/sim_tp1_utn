from PyQt5 import QtCore, QtGui, QtWidgets

class SecondViewWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultTable = QtWidgets.QTableView(self.centralwidget)
        self.resultTable.setGeometry(QtCore.QRect(440, 30, 361, 251))
        self.resultTable.setObjectName("resultTable")
        self.resultLbl = QtWidgets.QLabel(self.centralwidget)
        self.resultLbl.setGeometry(QtCore.QRect(600, 10, 61, 16))
        self.resultLbl.setObjectName("resultLbl")
        self.histogramaLbl = QtWidgets.QLabel(self.centralwidget)
        self.histogramaLbl.setGeometry(QtCore.QRect(200, 0, 101, 31))
        self.histogramaLbl.setObjectName("histogramaLbl")
        self.histogramaTable = QtWidgets.QGraphicsView(self.centralwidget)
        self.histogramaTable.setGeometry(QtCore.QRect(50, 30, 371, 251))
        self.histogramaTable.setObjectName("histogramaTable")
        self.JiCuadradoBox = QtWidgets.QSpinBox(self.centralwidget)
        self.JiCuadradoBox.setGeometry(QtCore.QRect(530, 590, 131, 22))
        self.JiCuadradoBox.setObjectName("JiCuadradoBox")
        self.jcTitleLbl = QtWidgets.QLabel(self.centralwidget)
        self.jcTitleLbl.setGeometry(QtCore.QRect(350, 300, 171, 16))
        self.jcTitleLbl.setObjectName("jcTitleLbl")
        self.JcLbl = QtWidgets.QLabel(self.centralwidget)
        self.JcLbl.setGeometry(QtCore.QRect(460, 590, 61, 16))
        self.JcLbl.setObjectName("JcLbl")
        self.jiCuadradoTable = QtWidgets.QTableView(self.centralwidget)
        self.jiCuadradoTable.setGeometry(QtCore.QRect(170, 330, 491, 251))
        self.jiCuadradoTable.setObjectName("jiCuadradoTable")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resultLbl.setText(_translate("MainWindow", "Resultados"))
        self.histogramaLbl.setText(_translate("MainWindow", "Histograma"))
        self.jcTitleLbl.setText(_translate("MainWindow", "Prueba de Bondad con Ji Cuadrado"))
        self.JcLbl.setText(_translate("MainWindow", "Ji Calculado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
