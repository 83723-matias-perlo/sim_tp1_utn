from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from matplotlib import pyplot as plt
from ..ui.secondView_ui import Ui_SecondViewWindow
from .paquetes.ji_cuadrado import generar_prueba_ji_cuadrado

class SecondView(QtWidgets.QDialog, Ui_SecondViewWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.return_2.clicked.connect(self.cerrar)

        #valores necesarios para realizar la visualizacion
        self.matriz_datos_generador_nros = []
        self.matriz_datos_prueba_ji_cuadrado = []
        self.frecuencias_observadas = []

    def set_calculos_del_generador(self, matriz):
        
        #guarda la matriz de datos
        self.matriz_datos_generador_nros = matriz

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
        '''setea las frecuencias observadas y con ellas realiza el histograma y
        la prueba ji cuadrado'''

        #guarda el arreglo
        self.frecuencias_observadas = frec

        #muestra el histograma en ventana separada
        self._crear_histograma()
        self._crear_prueba_ji_cuadrado()

    def _crear_histograma(self):
        '''crea el histograma'''

        frecs = self.frecuencias_observadas

        #esta iteracion convertira los contadores en valores medios 
        #de sus intervalos, para poder ser leidos por pyplot y
        #poder ser seteados en su secuencia correspondiente
        base = 0
        inc = 1 / len(frecs)
        valores_medios = []
        for frec in frecs:
            for i in range(frec):
                valores_medios.append(base + inc / 2)
            base += inc

        bins = []
        for i in range(len(frecs) + 1):
            bins.append(i / len(frecs))

        #pasamos los parametros al constructor
        plt.hist(
            x=valores_medios, 
            bins=bins,
            orientation="vertical", 
            color="green", 
            ec="black")
        
        #setear valores de presentacion y lanzar
        plt.xticks(bins)
        plt.title("Histograma de frecuencias")
        plt.xlabel('Intervalo')
        plt.ylabel('Frecuencia')
        plt.show()

    def _crear_prueba_ji_cuadrado(self):
        '''obtiene los resultados de la prueba, revisa que esten en orden y las muestra'''
        
        # obtiene los resultados con este modulo
        self.matriz_datos_prueba_ji_cuadrado = generar_prueba_ji_cuadrado(self.frecuencias_observadas)

        #los setea en la tabla
        rowPosition = 0
        matriz = self.matriz_datos_prueba_ji_cuadrado

        #inserta cada entrada
        for i in range(len(matriz)):
            self.jiCuadradoTable.insertRow(rowPosition)
            self.jiCuadradoTable.setItem(rowPosition , 0, QTableWidgetItem(str(matriz[i][0])))
            self.jiCuadradoTable.setItem(rowPosition , 1, QTableWidgetItem(str(matriz[i][1])))
            self.jiCuadradoTable.setItem(rowPosition , 2, QTableWidgetItem(str(matriz[i][2])))
            self.jiCuadradoTable.setItem(rowPosition , 3, QTableWidgetItem(str(matriz[i][3])))
            self.jiCuadradoTable.setItem(rowPosition , 4, QTableWidgetItem(str(matriz[i][4])))
            rowPosition += 1
        
        #por ultimo setea el Ji Calculado en el LineText
        self.JiCuadradoBox.setText(str(matriz[i][4]))
    
    def cerrar(self):
        plt.close()
        self.close()

if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = SecondView()
    window.show()
    app.exec_()