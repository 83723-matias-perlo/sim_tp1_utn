from  secondView_ui import *

GEN_NRO = ""
INTERVALO = ""
C = 0
G = 0
K = 0


class SecondView(QtWidgets.QMainWindow, SecondViewWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #asignar metodos
        print(C, G, K, GEN_NRO, INTERVALO)



if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()