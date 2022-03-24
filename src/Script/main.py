from  main_ui import *



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnAceptar.clicked.connect(aceptar)
        self.btnCancelar.clicked.connect(cancelar)

def aceptar():
    print("acepto")

def cancelar():
    print("cancelar")

def open():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

open()