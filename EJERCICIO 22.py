#*** zona funcion ***
def pedir_datos():
    numero_1 = int(input("Digite un mumero para la resta:"))
    numero_2 = int(input("Digite un numero para la resta:"))
    return numero_1, numero_2
def hacer_calculo(numero_1, numero_2):
    resta = numero_1 - numero_2
    return resta
def mostrar_resultado(suma):
    print("la resta de los dos numeros es "+ str(suma))




#*** codigo principal ***
numero_1, numero_2 = pedir_datos()
resta = hacer_calculo(numero_1, numero_2)
mostrar_resultado(resta)
