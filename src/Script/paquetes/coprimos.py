'''Modulo para calculo de factores primos y coprimos
'''

def es_coprimo(a, b):
    '''return si a es coprimo de b
    '''
    if 0 in [a, b]:
        return False
    if a < 0 or b < 0:
        return False
        
    factoresA = factores_primos(a)
    factoresB = factores_primos(b)
    for cop in factoresA:
        if cop in factoresB:
            return False
    return True


def factores_primos(x):
    '''hace un arreglo con los factores primos del numero
    '''
    factor = 2
    factores = []
    while factor <= x:
        if (x % factor == 0):
            factores.append(factor)
            x /= factor
        else:
            factor += 1
    return factores

if __name__ == "__main__":
    a = 7
    b = 780
    print("a:", a)
    print("b:", b)
    print("factores de a:", factores_primos(a))
    print("factores de b:", factores_primos(b))
    print("a y b son primos relativos:", es_coprimo(a, b))



