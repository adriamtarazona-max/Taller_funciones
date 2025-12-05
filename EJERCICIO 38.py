#*** zona funcion ***
def definir_datos():
    a = float(input("Digite el primer numero:"))
    b = float(input("Digite el segundo numero:"))
    return a, b
def hacer_calculo(a, b):
    mayor = (a + b + abs(a - b)) / 2
    return mayor
def mostrar_resultado(mayor):
    print("El numero mayor es:" + str(mayor))



#*** codigo principal ***
a, b = definir_datos()
mayor = hacer_calculo(a, b)
mostrar_resultado (mayor)
