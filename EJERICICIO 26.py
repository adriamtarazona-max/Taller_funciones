#*** zona funcion ***
def definir_datos():
    numero_1 = float(input("Digite un numero para la division de residuo:"))
    numero_2 = float(input("Digite otro numero para la division de residuo:"))
    return numero_1, numero_2
def hacer_calculo(numero_1, numero_2):
    residuo = numero_1 / numero_2
    return residuo
def mostrar_resultado(residuo):
    print("el residuo de la division es"+ str(residuo))



#*** codigo principal ***
numero_1, numero_2 = definir_datos()
residuo = hacer_calculo(numero_1, numero_2)
mostrar_resultado(residuo)
