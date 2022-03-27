'''Clases que contienen la logica, las condiciones y los metodos de calculo de cada generador'''

import random as rd
from coprimos import es_coprimo

class MetodoGeneradorNumeros:
    '''Metodo general, no se espera usar directamente
    '''
    #TODO: completar
    def __init__(self):
        self._semilla = 0
        self._a = 0
        self._m = 0
        self._c = 0
        self._g = 0
        self._k = 0
        self._cant_intervalos = 0
        self._intervalos_frecuencia = []
        self._matriz_calculos = []
        self._cant_filas_para_matriz = 0

    def obtener_matriz_valores_calculados(self):
        '''devuelve la matriz de los primeros calculos realizados para la generacion 
        de los nros + el ultimo calculo

        la matriz tiene como columnas : i , (a.X + c), Xi+1, RND
        la cantidad de filas dependera de la cantidad de entradas que se desee guardar
        puede setear la cantidad de filas en set_cant_filas_para_matriz(self, num) 
        '''
        return self._matriz_calculos
    
    def obtener_frecuencias_de_cada_intervalo(self):
        '''devuelve el array con los contadores para cada intervalo de frecuencia'''
        return self._intervalos_frecuencia

    def setG(self, g):
        if self.g_valido(g):
            self._g = g
            self.calcular_M()
            return g
        return -1

    def setK(self, k):
        if self.k_valido(k):
            self._k = k
            self.calcular_A()
            return k
        return -1
    
    def setC(self, c):
        if self.c_valido(c):
            self._c = c
            return c
        return -1
    
    def setSemilla(self, semilla):
        if self.semilla_valida(semilla):
            self._semilla = semilla
            return semilla
        return -1
    
    def set_cant_intervalos(self, cant):
        '''aca van la cantidad de intervalos requeridos'''
        self._cant_intervalos = cant
        self._intervalos_frecuencia = [0] * cant
        return cant

    def set_cant_filas_para_matriz(self, num):
        '''setea la cantidad de filas que quiero guardar (ademas de la ultima) para recuperar con 
        la matriz'''
        self._cant_filas_para_matriz = num
        return num

    def g_valido(self, g):
        pass

    def k_valido(self, k):
        pass

    def c_valido(self, c):
        pass
    
    def semilla_valida(self,semilla):
        pass

    def calcular_M(self):
        pass
    
    def calcular_A(self):
        pass

    def generar_numeros(self, cantNros):
        '''genera los numeros aleatorios, y setea los intervalos y matriz resultantes'''
        
        #cuenta la cant de filas guardadas de los calculos realizados
        filas_guardadas_ = 0
        guardado = False
        calculos_restantes = cantNros

        #valor inicial        
        xi1 = self._semilla

        #ancho del intervalo
        intervalo = 1 / self._cant_intervalos

        #for principal del calculo
        for i in range(cantNros):
            calc_sin_mod = self._calc_aX_c(xi1)
            xi1 = self._calc_xi1(calc_sin_mod)
            rnd = self._calc_RND(xi1)
            
            #hay mas filas por guardar?
            guardado = False
            if filas_guardadas_ <= self._cant_filas_para_matriz - 2:
                #crear una nueva entrada y guardarla, luego incrementar
                self._matriz_calculos.append([i + 1, calc_sin_mod, xi1, rnd])
                filas_guardadas_ += 1
                guardado = True

            #incrementar la frecuencia de los intervalos
            for i in range(self._cant_intervalos):
                if rnd <= ((i + 1) * intervalo) :
                    self._intervalos_frecuencia[i] += 1
                    break
        
            #decrementa los calculos que faltan
            calculos_restantes -= 1

            #es el ultimo calculo y no se ha guardado? entonces guardar
            if calculos_restantes == 0 and not guardado:
                self._matriz_calculos.append([cantNros, calc_sin_mod, xi1, rnd])
        

    #Metodos HOOK que varian durante la generacion segun el metodo
    def _calc_aX_c(self, xi1):
        '''calcula el (a.X + c) de la iteracion'''
        pass

    def _calc_xi1(self, calc_sin_mod):
        '''aplica mod sobre el parentesis ya calculado'''
        pass
    
    def _calc_RND(self, xi1):
        '''calcula el RND'''
        pass




class MetodoCongruencialLineal(MetodoGeneradorNumeros):
    '''Metodo Congruencial Lineal'''
    def __init__(self) -> None:
        super().__init__()

    def g_valido(self, g):
        return g > 0

    def k_valido(self, k):
        return k > 0

    def c_valido(self, c):
        return es_coprimo(c, self._m)
    
    def semilla_valida(self, semilla):
        return True

    def calcular_M(self):
        self._m = pow(2, self._g)
    
    def calcular_A(self):
        self._a = 1 + 4 * self._k

    def _calc_aX_c(self, xi1):
        '''calcula el (a.X + c) de la iteracion'''
        return self._a * xi1 + self._c

    def _calc_xi1(self, calc_sin_mod):
        '''aplica mod para (aX + c)mod(m)'''
        return calc_sin_mod % self._m
    
    def _calc_RND(self, xi1):
        '''calcula el RND'''
        return xi1 / self._m


class MetodoMultiplicativo(MetodoGeneradorNumeros):
    '''Metodo Multiplicativo'''
    def __init__(self) -> None:
        super().__init__()

    def g_valido(self, g):
        return g > 0

    def k_valido(self, k):
        return k >= 0
    
    def c_valido(self, c):
        return True
    
    def semilla_valida(self,semilla):
        return semilla > 0 and semilla % 2 != 0

    def calcular_M(self):
        self._m = pow(2, self._g)
    
    def calcular_A(self):
        self._a = 3 + 8 * self._k
    
    def _calc_aX_c(self, xi1):
        '''calcula el (a.X) de la iteracion'''
        return self._a * xi1

    def _calc_xi1(self, calc_sin_mod):
        '''aplica mod para (aX)mod(m)'''
        return calc_sin_mod % self._m
    
    def _calc_RND(self, xi1):
        '''calcula el RND'''
        return xi1 / self._m

class MetodoPython(MetodoGeneradorNumeros):
    '''Metodo generico de Python'''
    def __init__(self) -> None:
        super().__init__()

    def g_valido(self, g):
        return True

    def k_valido(self, k):
        return True

    def c_valido(self, c):
        return True
    
    def semilla_valida(self,semilla):
        return True

    def _calc_aX_c(self, xi1):
        '''retorna 0'''
        return 0

    def _calc_xi1(self, calc_sin_mod):
        '''retorna 0'''
        return 0
    
    def _calc_RND(self, xi1):
        '''calcula el RND'''
        return rd.random() % 1

if __name__ == "__main__":
    print(MetodoCongruencialLineal().setG(4))
    for i in range(10):
        print(rd.random() % 1)