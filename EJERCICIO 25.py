#*** zona funcion ***
def pedir_datos():
    numero_1 = float(input("Digite un numero para la divicion:"))
    numero_2 = float(input("Digite otro numero para la divicion:"))
    return numero_1, numero_2
def hacer_calculo(numero_1, numero_2):
    division = numero_1 / numero_2
    return division
def mostrar_resulatado(division):
    print("La division de los dos numeros es"+ str(division))



#*** codigo principal ***
numero_1, numero_2 = pedir_datos()
division = hacer_calculo(numero_1, numero_2)
mostrar_resulatado (division)
