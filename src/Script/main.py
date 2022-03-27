
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from main_ui import Ui_MainWindow
from metodos import MetodoCongruencialLineal, MetodoMultiplicativo, MetodoPython
from secondView import SecondView


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        
        #una lista de los metodos que pueden utilizarse, y el metodo actual (Mixto por defecto)
        self.metodos = [MetodoCongruencialLineal, MetodoMultiplicativo, MetodoPython]
        self.metodo = MetodoCongruencialLineal()

        self.setupUi(self)
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(self.cancelar)

        # Cada vez que se elija un generador, ejecuta el metodo 'restringir_variables'.
        self.cmbGeneradorNros.activated[str].connect(self.restringir_variables)

    # Restringe los inputs dependiendo del tipo de generador que seleccionemos.
    def restringir_variables(self):
        self.metodo = self.metodos[self.cmbGeneradorNros.currentIndex()]()
        #self.tipo_generador = self.cmbGeneradorNros.currentIndex()

        if self.metodo.__class__ == MetodoMultiplicativo:
            # Si el generador es Congruencial Multiplicativo, deshabilita el input para 'c'.
            self.cBox.setDisabled(True)
            self.cBox.setText("0")

        elif self.metodo.__class__ == MetodoPython:
            # Si el generador es una funcion del lenguaje, deshabilita todos los inputs.
            self.cBox.setDisabled(True)
            self.cBox.setText("0")
            self.gBox.setDisabled(True)
            self.gBox.setText("0")
            self.kBox.setDisabled(True)
            self.kBox.setText("0")

        else:
            # Si no cumple ninguno, significa que esta en Congruencial Lineal y habilita todos los inputs.
            self.cBox.setDisabled(False)
            self.gBox.setDisabled(False)
            self.kBox.setDisabled(False)

    def setear_valores_a_metodo(self):
        if self.metodo.setG(int(self.gBox.text())) == -1:
            QMessageBox.about(self, "Error", "La constante G es invalida para el metodo seleccionado")
            return False
        if self.metodo.setK(int(self.kBox.text())) == -1:
            QMessageBox.about(self, "Error", "La constante K es invalida para el metodo seleccionado")
            return False
        if self.metodo.setC(int(self.cBox.text())) == -1:
            QMessageBox.about(self, "Error", "La constante C es invalida para el metodo seleccionado")
            return False
        if self.metodo.setSemilla(int(self.semillaBox.text())) == -1:
            QMessageBox.about(self, "Error", "La semilla es invalida para el metodo seleccionado")
            return False

        self.metodo.set_cant_intervalos(int(self.cmbIntervalos.currentText()))
        self.metodo.set_cant_filas_para_matriz(12) #Hardcodeado, no se espera que varie

        return True


    def aceptar(self):
        # revisa que no haya campos vacios, si los hay, cancelar y los resetea
        if self.hay_campos_vacios():
            QMessageBox.about(self, "Error", "exiten campos sin rellenar")
            self.resetear_campos()
            return
        
        #Antes de comenzar a validar, asumimos que todo anda bien, hasta que se demuestre lo contrario
        if not self.setear_valores_a_metodo():
            self.metodo = self.metodos[self.cmbGeneradorNros.currentIndex()]()
            return

        #solo llega aca habiendo validado el resto
        

        #activamos el metodo ya seteado para que haga los calculos
        self.metodo.generar_numeros(int(self.cantNrosBox.text()))

        #creamos la ventana seteada con los resultados y la lanzamos
        self.close()
        #self.ventana = QtWidgets.QMainWindow()
        self.secView = SecondView()
        self.secView.set_frecuencias_observadas(self.metodo.obtener_frecuencias_de_cada_intervalo())
        self.secView.set_calculos_del_generador(self.metodo.obtener_matriz_valores_calculados())
        #self.ui.setupUi(self.ventana)
        self.secView.show()

    def cancelar(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
