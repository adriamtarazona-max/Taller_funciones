#*** zona fucion ***
def definir_datos():
    numero_1 = int(input("Digite un numero:"))
    numero_2 = int(input("Digite un numero:"))
    return numero_1, numero_2
def hacer_calculo(numero_1, numero_2):
    cuadrado = numero_1 * numero_2
    return cuadrado
def mostrar_resultado(cuadrado):
    print("El cuadrado de los dos numeros es"+ str(cuadrado))




#*** codigo principal ***
numero_1, numero_2 = definir_datos()
cuadrado = hacer_calculo(numero_1, numero_2)
mostrar_resultado(cuadrado)
