#*** zona funcion ***
def pedir_datos():
    numero_1 = int(input("Digite un numero para la suma:"))
    numero_2 = int(input("Digite un numero para la suma:"))
    return numero_1, numero_2
def hacer_calculo(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma
def mostrar_resultado(suma):
    print("la suma de los dos numero es:"+ str(suma))



#*** codigo principal ***
numero_1, numero_2 = pedir_datos()
suma = hacer_calculo(numero_1,numero_2)
mostrar_resultado(suma)
