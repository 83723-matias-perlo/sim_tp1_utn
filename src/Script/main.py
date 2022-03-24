from main_ui import *
from PyQt5 import QtWidgets
from secondView import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(self.cancelar)

    def aceptar (self):
        #crear metodo de validar si se cargaron todos los valores

        self.close()
        self.ventana = QtWidgets.QMainWindow()
        self.ui = SecondView()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def cancelar(self):
        self.close()

if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

