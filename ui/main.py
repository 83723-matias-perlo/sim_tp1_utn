# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(289, 386)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 330, 151, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 251, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 91, 20))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 90, 191, 121))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(100, 50, 81, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 80, 81, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 20, 81, 21))
        self.textEdit_3.setReadOnly(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 290, 47, 13))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(140, 290, 104, 21))
        self.textEdit_4.setObjectName("textEdit_4")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 250, 251, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(120, 230, 71, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Generador de Nros"))
        self.groupBox.setTitle(_translate("Dialog", "Constantes"))
        self.label_2.setText(_translate("Dialog", "g"))
        self.label_3.setText(_translate("Dialog", "k"))
        self.label_4.setText(_translate("Dialog", "c"))
        self.label_5.setText(_translate("Dialog", "semilla"))
        self.label_6.setText(_translate("Dialog", "Intervalos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
