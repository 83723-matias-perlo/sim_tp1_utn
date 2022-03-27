# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(292, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblGeneradorNro = QtWidgets.QLabel(self.centralwidget)
        self.lblGeneradorNro.setGeometry(QtCore.QRect(100, 10, 101, 20))
        self.lblGeneradorNro.setMaximumSize(QtCore.QSize(101, 16777215))
        self.lblGeneradorNro.setObjectName("lblGeneradorNro")
        self.cmbGeneradorNros = QtWidgets.QComboBox(self.centralwidget)
        self.cmbGeneradorNros.setGeometry(QtCore.QRect(30, 130, 231, 22))
        self.cmbGeneradorNros.setObjectName("cmbGeneradorNros")
        self.cmbGeneradorNros.addItem("")
        self.cmbGeneradorNros.addItem("")
        self.cmbGeneradorNros.addItem("")
        self.cmbIntervalos = QtWidgets.QComboBox(self.centralwidget)
        self.cmbIntervalos.setGeometry(QtCore.QRect(20, 330, 251, 22))
        self.cmbIntervalos.setObjectName("cmbIntervalos")
        self.cmbIntervalos.addItem("")
        self.cmbIntervalos.addItem("")
        self.cmbIntervalos.addItem("")
        self.cmbIntervalos.addItem("")
        self.IntervalosLabel = QtWidgets.QLabel(self.centralwidget)
        self.IntervalosLabel.setGeometry(QtCore.QRect(120, 310, 71, 16))
        self.IntervalosLabel.setObjectName("IntervalosLabel")
        self.semillaLabel = QtWidgets.QLabel(self.centralwidget)
        self.semillaLabel.setGeometry(QtCore.QRect(60, 370, 47, 13))
        self.semillaLabel.setObjectName("semillaLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 170, 191, 121))
        self.groupBox.setObjectName("groupBox")
        self.gLabel = QtWidgets.QLabel(self.groupBox)
        self.gLabel.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.gLabel.setObjectName("gLabel")
        self.kLabel = QtWidgets.QLabel(self.groupBox)
        self.kLabel.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.kLabel.setObjectName("kLabel")
        self.cLabel = QtWidgets.QLabel(self.groupBox)
        self.cLabel.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.cLabel.setObjectName("cLabel")
        self.cBox = QtWidgets.QLineEdit(self.groupBox)
        self.cBox.setGeometry(QtCore.QRect(90, 20, 81, 20))
        self.cBox.setObjectName("cBox")
        self.gBox = QtWidgets.QLineEdit(self.groupBox)
        self.gBox.setGeometry(QtCore.QRect(90, 50, 81, 20))
        self.gBox.setObjectName("gBox")
        self.kBox = QtWidgets.QLineEdit(self.groupBox)
        self.kBox.setGeometry(QtCore.QRect(90, 80, 81, 20))
        self.kBox.setObjectName("kBox")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(60, 440, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(160, 440, 75, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.cantNumerosLabel = QtWidgets.QLabel(self.centralwidget)
        self.cantNumerosLabel.setGeometry(QtCore.QRect(70, 40, 141, 16))
        self.cantNumerosLabel.setObjectName("cantNumerosLabel")
        self.tipoGeneradorLabel = QtWidgets.QLabel(self.centralwidget)
        self.tipoGeneradorLabel.setGeometry(QtCore.QRect(80, 110, 141, 16))
        self.tipoGeneradorLabel.setObjectName("tipoGeneradorLabel")
        self.cantNrosBox = QtWidgets.QLineEdit(self.centralwidget)
        self.cantNrosBox.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.cantNrosBox.setObjectName("cantNrosBox")
        
        self.semillaBox = QtWidgets.QLineEdit(self.centralwidget)
        self.semillaBox.setGeometry(QtCore.QRect(140, 370, 81, 20))
        self.semillaBox.setObjectName("semillaBox")
        

        #Las modificaciones manuales sobre la interfaz estan aca
        intValidator = QIntValidator(0, 1000000)
        intValidatorCant = QIntValidator(30, 1000000)

        #validadores de enteros
        self.cBox.setValidator(intValidator)
        self.gBox.setValidator(intValidator)
        self.kBox.setValidator(intValidator)
        self.cantNrosBox.setValidator(intValidatorCant)
        self.semillaBox.setValidator(intValidator)
        
        #insertar valores iniciales
        self.resetear_campos()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # -------- FUNCIONES AGREGADAS MANUALMENTE
    def resetear_campos(self):
        '''inserta los valores iniciales de los inputs
        '''
        self.cBox.setText("0")
        self.gBox.setText("0")
        self.kBox.setText("0")
        self.cantNrosBox.setText("30")
        self.semillaBox.setText("0")

    def hay_campos_vacios(self):
        '''Avisa si dejaron alguno de los campos sin ninguna entrada'''
        return "" in [
            self.cBox.text(),
            self.gBox.text(),
            self.kBox.text(),
            self.cantNrosBox.text(),
            self.semillaBox.text()
        ]
    # ------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblGeneradorNro.setText(_translate("MainWindow", "Generador de Nros"))
        self.cmbGeneradorNros.setItemText(0, _translate("MainWindow", "Congruencial Lineal"))
        self.cmbGeneradorNros.setItemText(1, _translate("MainWindow", "Cungruencial Multiplicativo"))
        self.cmbGeneradorNros.setItemText(2, _translate("MainWindow", "Funcion del Lenguaje (Python)"))
        self.cmbIntervalos.setItemText(0, _translate("MainWindow", "5"))
        self.cmbIntervalos.setItemText(1, _translate("MainWindow", "10"))
        self.cmbIntervalos.setItemText(2, _translate("MainWindow", "15"))
        self.cmbIntervalos.setItemText(3, _translate("MainWindow", "20"))
        self.IntervalosLabel.setText(_translate("MainWindow", "Intervalos"))
        self.semillaLabel.setText(_translate("MainWindow", "semilla"))
        self.groupBox.setTitle(_translate("MainWindow", "Constantes"))
        self.gLabel.setText(_translate("MainWindow", "g"))
        self.kLabel.setText(_translate("MainWindow", "k"))
        self.cLabel.setText(_translate("MainWindow", "c"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.cantNumerosLabel.setText(_translate("MainWindow", "Cant de numero para generar"))
        self.tipoGeneradorLabel.setText(_translate("MainWindow", "Tipo de Generador a usar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
