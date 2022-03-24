#funcion metodo congruencial lineal
#X0 es la semilla
# - a es la constante multiplicativa
# - c es una constante aditiva
# - m es el módulo
def metodo_congruencial_multiplicativo(a,m,x0,n):
    x = []
    x.append(x0)
    vec_aleatorio = []
    for i in range(1,n):
        x.append(a*x[i-1]%m)
        vec_aleatorio.append(x[i]/(m))

    return vec_aleatorio


#funcion metodo congruencial multiplicativo
#X0 es la semilla
# a es la constante multiplicativa
# m es el módulo
def congruencia_Lineal (a,m,x0,n,c):
    x = []
    x.append(x0)
    vec_aleatorio = []
    for i in range(1, n):
        x.append((a * x[i - 1]+c) % m)
        vec_aleatorio.append(x[i] / (m))
    return vec_aleatorio

#funcion ji-cuadrada
#frecuencia observada
# fe: frecuencia esperada
# k: cantidad de clases o intervalos
# m: cantidad de datos empíricos
# v: grados de libertad
def metodo_ji_cuadrada(a,m,x0,n):
    x = []
    x.append(x0)
    for i in range(1,n):
        x.append((a*x[i-1]**2)%m)
    return x

#crear class main
class main():
    def __init__(self):
        pass
    def main(self):
        pass

def validar_Numero():
    x = input("ingrese un numero: ")
    if x.isdigit():
        return x
    else:
        print("no es un numero")
        return validar()

validar_Numero()
