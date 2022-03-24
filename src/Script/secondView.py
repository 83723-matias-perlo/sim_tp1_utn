from  secondView_ui import *

class SecondView(QtWidgets.QMainWindow, SecondViewWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #asignar metodos



if __name__ == "__main__":  
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()