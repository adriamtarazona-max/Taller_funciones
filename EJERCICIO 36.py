#*** zona funcion ***
def pedir_datos():
    a = float(input("Digite el numero de division entera:"))
    b = float(input("Digite el segundo numero de division entera:"))
    return a, b
def hacer_calculo(a, b):
    cociente = a // b
    return cociente
def mostrar_resultado(cociente):
    print("El cociente es"+ str(cociente))
    
    
#*** codigo funcion ***
a, b= pedir_datos()
cociente=hacer_calculo(a, b)
mostrar_resultado(cociente)

