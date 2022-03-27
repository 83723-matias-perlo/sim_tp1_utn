from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from matplotlib import pyplot as plt
from  secondView_ui import Ui_SecondViewWindow

class SecondView(QtWidgets.QMainWindow, Ui_SecondViewWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        #valores necesarios para realizar la visualizacion
        self.matriz_valores_calculados = []
        self.frecuencias_observadas = []

    def set_calculos_del_generador(self, matriz):
        
        #guarda la matriz de datos
        self.matriz_valores_calculados = matriz

        #contador de las entradas
        rowPosition = 0

        #inserta cada entrada
        for i in range(len(matriz)):
            self.resultTable.insertRow(rowPosition)
            self.resultTable.setItem(rowPosition , 0, QTableWidgetItem(str(matriz[i][0])))
            self.resultTable.setItem(rowPosition , 1, QTableWidgetItem(str(matriz[i][1])))
            self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(str(matriz[i][2])))
            self.resultTable.setItem(rowPosition , 3, QTableWidgetItem(str(matriz[i][3])))
            rowPosition += 1
    
    def set_frecuencias_observadas(self, frec):

        #guarda el arreglo
        self.frecuencias_observadas = frec

        #muestra el histograma en ventana separada
        plt.hist(x=frec, bins=len(frec), orientation="vertical", color="green", ec="black")
        plt.xticks(frec)
        plt.title("Histograma de frecuencias")
        plt.xlabel('Intervalo')
        plt.ylabel('Frecuencia')
        plt.show()

    



if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = SecondView()
    window.show()
    app.exec_()