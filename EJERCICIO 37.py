#*** zona funcion ***
def pedir_datos():
    a = int(input("Digite el primer numero:"))
    b = int(input("Digite el segundo numero:"))
    return a, b
def hacer_calculo(a,b):
    if a % b == 0:
        mensaje = a, "es multiplo de", b
    else:
        mensaje = a, " no es multiplo de", b
    return mensaje
def mostrar_resultado(mensaje):
    print("el multiplo es:" + str(mensaje))



#**** codigo principal ****
a, b = pedir_datos()
mensaje = hacer_calculo(a, b)
mostrar_resultado(mensaje)
