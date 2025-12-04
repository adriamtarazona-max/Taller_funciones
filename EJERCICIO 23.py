#*** zona funcion ***
def pedir_datos():
    numero_1 = int(input("Digite el numero para la multiplicacion:"))
    numero_2 = int(input("Digite el numero para la multiplicacion:"))
    return numero_1, numero_2
def hacer_calculo(numero_1, numero_2):
    mult = numero_1 * numero_2
    return mult
def mostrar_resultado(mult):
    print("la multiplicacion de los dos numeros es:"+ str(mult))




#**** codigo prnicipal ****
numero_1, numero_2 = pedir_datos()
mult = hacer_calculo(numero_1, numero_2)
mostrar_resultado(mult)
    