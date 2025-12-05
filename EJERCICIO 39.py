#*** zona funcion ***
def pedir_datos():
    a = float(input("Digite un numero:"))
    b = float(input("Digite un numero:"))
    return a, b
def hacer_calculo(a, b):
    promedio= a + b / 2
    return promedio
def mostrar_resultado(promedio):
    print("El promedio del numero es"+ str(promedio))



#*** codigo principal ***
a, b = pedir_datos()
promedio = hacer_calculo(a, b)
mostrar_resultado(promedio)
