def Crear_Histograma1(vector_frecuencias, cant_intervalos):
    
    import pandas as pd
    import matplotlib.pyplot as plt

    tamaño_intervalo = 1/cant_intervalos
    vector_intervalos = []
    limite=0
    for i in range (cant_intervalos+2):
        vector_intervalos.append(limite)
        limite = i*tamaño_intervalo


    print(len(vector_intervalos))



    plt.hist(x=vector_frecuencias, bins=cant_intervalos, orientation="vertical", color="green", ec="black")
    plt.xticks(vector_intervalos)
    plt.title("Histograma de frecuencias")
    plt.xlabel('Intervalo')
    plt.ylabel('Frecuencia')
    plt.show()
