from PyQt5.QtWidgets import QMessageBox
from main_ui import *
import secondView as s


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.ok = False
        self.m_value = 0
        self.a_value = 0
        self.c_value = 0
        self.x0_value = 0
        self.intervalos = 0
        self.setupUi(self)
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tipo_generador = self.cmbGeneradorNros.currentIndex()
        # Cada vez que se elija un generador, ejecuta el metodo 'restringir_variables'.
        self.cmbGeneradorNros.activated[str].connect(self.restringir_variables)

    # Restringe los inputs dependiendo del tipo de generador que seleccionemos.
    def restringir_variables(self):
        self.tipo_generador = self.cmbGeneradorNros.currentIndex()
        if self.tipo_generador == 1:
            # Si el generador es Congruencial Multiplicativo, deshabilita el input para 'c'.
            self.cBox.setDisabled(True)
            self.cBox.setValue(0)
        elif self.tipo_generador == 2:
            # Si el generador es una funcion del lenguaje, deshabilita todos los inputs.
            self.cBox.setDisabled(True)
            self.cBox.setValue(0)
            self.gBox.setDisabled(True)
            self.gBox.setValue(0)
            self.kBox.setDisabled(True)
            self.kBox.setValue(0)
        else:
            # Si no cumple ninguno, significa que esta en Congruencial Lineal y habilita todos los inputs.
            self.cBox.setDisabled(False)
            self.gBox.setDisabled(False)
            self.kBox.setDisabled(False)

    def aceptar(self):
      
        self.generate_m_value()
        self.generate_a_value()
        self.set_c_value()
        self.set_x0_value()
        self.set_intervalos()
        print("Constante m: %i" % self.m_value)
        print("Constante a: %i" % self.a_value)
        print("Constante c: %i" % self.c_value)
        print("Constante X0 (semilla): %i" % self.x0_value)
        print("Intervalos: %i" % self.intervalos)

        if self.ok:
            # Si todas las validaciones fueron correctas, se procede a la siguiente pantalla. Sino queda validando
            # hasta que sean correctos los inputs.
            s.GEN_NRO = self.cmbGeneradorNros.currentText()
            s.INTERVALO = self.cmbIntervalos.currentText()
            s.C = self.cBox.value()
            s.G = self.gBox.value()
            s.K = self.kBox.value()
            self.close()
            self.ventana = QtWidgets.QMainWindow()
            self.ui = s.SecondView()
            self.ui.setupUi(self.ventana)
            self.ventana.show()

    def cancelar(self):
        self.close()

    # Genera el valor de 'm' a partir de la constante 'g'.
    def generate_m_value(self):
        self.m_value = 2 ** self.gBox.value()
        self.validar_constantes("m", self.m_value, self.tipo_generador)

    # Genera el valor de 'a' a partir de la constante 'k' dependiendo del tipo de generador.
    def generate_a_value(self):
        if self.tipo_generador == 0:
            # Si es un generador Congruencial Lineal: 1 + (4 * k)
            self.a_value = 1 + (4 * self.kBox.value())
        elif self.tipo_generador == 1:
            # Si es un generador Congruencial Multiplicativo: 3 + (8 * k)
            self.a_value = 3 + (8 * self.kBox.value())
        self.validar_constantes("a", self.a_value, self.tipo_generador)

    def set_c_value(self):
        # TODO: Para Lineal 'c' debe ser relativamente primo a 'm'
        self.c_value = self.cBox.value()

    def set_x0_value(self):
        self.x0_value = self.semillaBox.value()
        self.validar_constantes("x0", self.x0_value, self.tipo_generador)

    def validar_constantes(self, constante, valor, generador):
        if constante == "x0" and generador == 1:
            if valor <= 0:
                self.ok = False
                QMessageBox.about(self, "Error", "La constante '" + constante + "' debe ser un entero positivo")
            elif valor % 2 == 0:
                self.ok = False
                QMessageBox.about(self, "Error", "La constante '" + constante + "' debe ser un numero impar")
            else:
                self.ok = True
            # TODO: Si cumple ambos, sugerir que sea primo?
        elif constante == "m" or constante == "a" or constante == "x0":
            if valor <= 0:
                self.ok = False
                QMessageBox.about(self, "Error", "La constante '" + constante + "' debe ser un entero positivo")
            else:
                self.ok = True

    def set_intervalos(self):
        self.intervalos = int(self.cmbIntervalos.currentText())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
