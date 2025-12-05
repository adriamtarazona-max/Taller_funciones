#*** zona funcion ***
def definir_dato():
    cantidad_dinero = float(input("Digite la cantidad de dinero:"))
    return cantidad_dinero
def hacer_calculo(cantidad_dinero):
    interes = cantidad_dinero * 0.05 
    return interes
def mostra_resultado(interes):
    print("El interes generado es"+ str(interes))





#*** codigo principal ***
cantidad_dinero = definir_dato()
interes = hacer_calculo(cantidad_dinero)
mostra_resultado(interes)
