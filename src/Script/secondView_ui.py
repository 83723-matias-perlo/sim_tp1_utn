# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondView2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondViewWindow(object):
    def setupUi(self, SecondViewWindow):
        SecondViewWindow.setObjectName("SecondViewWindow")
        SecondViewWindow.resize(602, 615)
        self.centralwidget = QtWidgets.QWidget(SecondViewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultLbl = QtWidgets.QLabel(self.centralwidget)
        self.resultLbl.setGeometry(QtCore.QRect(270, 10, 61, 16))
        self.resultLbl.setObjectName("resultLbl")
        self.jcTitleLbl = QtWidgets.QLabel(self.centralwidget)
        self.jcTitleLbl.setGeometry(QtCore.QRect(210, 290, 171, 16))
        self.jcTitleLbl.setObjectName("jcTitleLbl")
        self.JcLbl = QtWidgets.QLabel(self.centralwidget)
        self.JcLbl.setGeometry(QtCore.QRect(360, 570, 61, 16))
        self.JcLbl.setObjectName("JcLbl")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(10, 570, 331, 23))
        self.return_2.setObjectName("return_2")
        self.resultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.resultTable.setGeometry(QtCore.QRect(10, 30, 581, 251))
        self.resultTable.setAutoScroll(True)
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTable.setDragDropOverwriteMode(False)
        self.resultTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.resultTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resultTable.setGridStyle(QtCore.Qt.SolidLine)
        self.resultTable.setWordWrap(False)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(4)
        self.resultTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(3, item)
        self.resultTable.horizontalHeader().setVisible(True)
        self.resultTable.horizontalHeader().setCascadingSectionResizes(False)
        self.resultTable.horizontalHeader().setDefaultSectionSize(135)
        self.resultTable.horizontalHeader().setHighlightSections(False)
        self.resultTable.horizontalHeader().setSortIndicatorShown(False)
        self.resultTable.horizontalHeader().setStretchLastSection(True)
        self.resultTable.verticalHeader().setVisible(False)
        self.resultTable.verticalHeader().setDefaultSectionSize(20)
        self.jiCuadradoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.jiCuadradoTable.setGeometry(QtCore.QRect(10, 310, 581, 251))
        self.jiCuadradoTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.jiCuadradoTable.setDragDropOverwriteMode(False)
        self.jiCuadradoTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.jiCuadradoTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.jiCuadradoTable.setWordWrap(False)
        self.jiCuadradoTable.setObjectName("jiCuadradoTable")
        self.jiCuadradoTable.setColumnCount(5)
        self.jiCuadradoTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jiCuadradoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jiCuadradoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jiCuadradoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jiCuadradoTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jiCuadradoTable.setHorizontalHeaderItem(4, item)
        self.jiCuadradoTable.horizontalHeader().setDefaultSectionSize(115)
        self.jiCuadradoTable.horizontalHeader().setHighlightSections(False)
        self.jiCuadradoTable.horizontalHeader().setStretchLastSection(True)
        self.jiCuadradoTable.verticalHeader().setVisible(False)
        self.jiCuadradoTable.verticalHeader().setDefaultSectionSize(20)
        self.JiCuadradoBox = QtWidgets.QLineEdit(self.centralwidget)
        self.JiCuadradoBox.setEnabled(True)
        self.JiCuadradoBox.setGeometry(QtCore.QRect(430, 570, 161, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JiCuadradoBox.sizePolicy().hasHeightForWidth())
        self.JiCuadradoBox.setSizePolicy(sizePolicy)
        self.JiCuadradoBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.JiCuadradoBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.JiCuadradoBox.setDragEnabled(True)
        self.JiCuadradoBox.setReadOnly(True)
        self.JiCuadradoBox.setObjectName("JiCuadradoBox")

        #si es un qdialog, el statusbar y centralwidget no van
        SecondViewWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SecondViewWindow)
        self.statusbar.setObjectName("statusbar")
        SecondViewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondViewWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondViewWindow)

    def retranslateUi(self, SecondViewWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondViewWindow.setWindowTitle(_translate("SecondViewWindow", "MainWindow"))
        self.resultLbl.setText(_translate("SecondViewWindow", "Resultados"))
        self.jcTitleLbl.setText(_translate("SecondViewWindow", "Prueba de Bondad con Ji Cuadrado"))
        self.JcLbl.setText(_translate("SecondViewWindow", "Ji Calculado"))
        self.return_2.setText(_translate("SecondViewWindow", "Return"))
        item = self.resultTable.horizontalHeaderItem(0)
        item.setText(_translate("SecondViewWindow", "i"))
        item = self.resultTable.horizontalHeaderItem(1)
        item.setText(_translate("SecondViewWindow", "(a.X +c)"))
        item = self.resultTable.horizontalHeaderItem(2)
        item.setText(_translate("SecondViewWindow", "Xi+1"))
        item = self.resultTable.horizontalHeaderItem(3)
        item.setText(_translate("SecondViewWindow", "RND"))
        item = self.jiCuadradoTable.horizontalHeaderItem(0)
        item.setText(_translate("SecondViewWindow", "Intervalo"))
        item = self.jiCuadradoTable.horizontalHeaderItem(1)
        item.setText(_translate("SecondViewWindow", "fo"))
        item = self.jiCuadradoTable.horizontalHeaderItem(2)
        item.setText(_translate("SecondViewWindow", "fe"))
        item = self.jiCuadradoTable.horizontalHeaderItem(3)
        item.setText(_translate("SecondViewWindow", "C"))
        item = self.jiCuadradoTable.horizontalHeaderItem(4)
        item.setText(_translate("SecondViewWindow", "C(AC)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondViewWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondViewWindow()
    ui.setupUi(SecondViewWindow)
    SecondViewWindow.show()
    sys.exit(app.exec_())