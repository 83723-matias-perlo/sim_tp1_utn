from  secondView_ui import *
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

class SecondView(QtWidgets.QMainWindow, Ui_SecondViewWindow):
    def __init__(self, *args, **kwargs):

        #valores necesarios para realizar la visualizacion
        self.matriz_valores_calculados = []
        self.frecuencias_observadas = []

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def set_matriz_valores_calculados(self, matriz):
        self.matriz_valores_calculados = matriz
        self.cargar_tabla_resultados(matriz)
        #rowPosition = self.resultTable.rowCount()
        #self.resultTable.setRowCount(len(matriz))
        #for i in range(len(matriz)):
        #    self.resultTable.insertRow(rowPosition)
        #    self.resultTable.setItem(rowPosition , 0, QTableWidgetItem(str(matriz[i][0])))
        #    self.resultTable.setItem(rowPosition , 1, QTableWidgetItem(str(matriz[i][1])))
        #    self.resultTable.setItem(rowPosition , 2, QTableWidgetItem(str(matriz[i][2])))
        #    self.resultTable.setItem(rowPosition , 3, QTableWidgetItem(str(matriz[i][3])))
        #    rowPosition += 1
            #self.resultTable.insertRow(rowPosition)
            #self.resultTable.setItem(matriz[i][0] , matriz[i][1], matriz[i][2], matriz[i][3])
            #self.resultTable.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        #TODO: relacionar esto con la tabla a mostrar
    
    def set_frecuencias_observadas(self, frec):
        self.frecuencias_observadas = frec
        #TODO: relacionarlo con el histograma del matplotlib



if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = Ui_SecondViewWindow() #TODO: este se rompio no se como repararlo jaja
    window.show()
    app.exec_()