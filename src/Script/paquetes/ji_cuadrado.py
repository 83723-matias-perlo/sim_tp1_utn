'''aca se calcula el ji cuadrado'''
import math

def truncar(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def generar_prueba_ji_cuadrado(frecuencias_observadas):
    '''hace la prueba del ji cuadrado y setea los valores en la tabla
    el formato de la matriz es de tipo: intervalo - fo - fe - C - C(AC)s
    '''

    #seteo cuantos decimales quiero por valor

    #valores para calcular el fe
    frecs = frecuencias_observadas
    total = 0
    fe = 0

    #obtener frecuencia esperada, 
    #siempre es dist. uniforme asique sera (total / cant_intervalos)
    for frec in frecs:
        total += frec
    fe = total / len(frecs)

    #validacion para saber si la frecuencia es el minimo esperado
    if(fe < 5):
        #TODO: no se si algo deberiamos hacer cuando el fe sea menor a 5
        pass  

    #valores para gestionar los intervalos y los calculos
    base = 0
    inc = 1 / len(frecs)
    C = 0
    CAC = 0

    #matriz de resultados
    matriz_datos_prueba_ji_cuadrado = []
    
    #iteracion principal
    for fo in frecs:
        C = truncar(pow(fo - fe, 2) / fe, 4)
        CAC = truncar(CAC + C, 4)

        #los datos se agregan a la matriz utilizando Decimal()
        #para poder truncarse en 4 decimales
        matriz_datos_prueba_ji_cuadrado.append([
            "{} - {}".format(str(truncar(base, 2)), str(truncar(base + inc, 2))),
            fo,
            truncar(fe, 4),
            C,
            CAC])
        base += inc
    
    return matriz_datos_prueba_ji_cuadrado

if __name__ == "__main__":
    #colocar aca cualquier test a realizar
    matriz = generar_prueba_ji_cuadrado([8,7,5,4,6])
    print("listo: \n", matriz)