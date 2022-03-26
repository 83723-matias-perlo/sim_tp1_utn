from  secondView_ui import *

class SecondView(QtWidgets.QMainWindow, SecondViewWindow):
    def __init__(self, *args, **kwargs):

        #valores necesarios para realizar la visualizacion
        self.matriz_valores_calculados = []
        self.frecuencias_observadas = []

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def set_matriz_valores_calculados(self, matriz):
        self.matriz_valores_calculados = matriz
        #TODO: relacionar esto con la tabla a mostrar
    
    def set_frecuencias_observadas(self, frec):
        self.frecuencias_observadas = frec
        #TODO: relacionarlo con el histograma del matplotlib



if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()