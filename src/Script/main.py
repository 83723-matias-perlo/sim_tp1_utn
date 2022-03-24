from email.policy import default
from main_ui import *
from PyQt5 import QtWidgets
import secondView as s

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(self.cancelar)


    def aceptar (self):
        #crear metodo de validar si se cargaron todos los valores
        tipoGenerador = self.cmbGeneradorNros.currentText()
        intervalos = self.cmbIntervalos.currentText()
        #print(tipoGenerador, intervalos)

        s.C = self.cBox.value()
        s.G = self.gBox.value()
        s.K = self.kBox.value()
        s.GEN_NRO = "Generador X"
        s.INTERVALO = "Intervalo Y"
        self.close()
        self.ventana = QtWidgets.QMainWindow()
        self.ui = s.SecondView()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def cancelar(self):
        self.close()

def validar(self):
    if self.cBox.value() == 0 or self.gBox.value() == 0 or self.kBox.value() == 0:
        return False

    
if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

