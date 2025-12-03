#*** zona funcion ***
def pedir_libra():
    libra = float(input("Digite cuantas libras va a pasar a kilogramos:"))
    return libra
def hacer_calculo(libra):
    k = 0.454 * libra
    return k
def mostrar_resultado(k):
    print("sus kilogramos en libras es"+ str(k))



#*** codigo principal ***
libra = pedir_libra()
k = hacer_calculo(libra)
mostrar_resultado(k)
    