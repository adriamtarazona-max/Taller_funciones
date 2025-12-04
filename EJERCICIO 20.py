#*** zona funcion ***
def pedir_litros():
    litros = float(input("Digite cunatos litros va a pasar a galones:"))
    return litros
def hacer_calculo(litros):
    g = litros / 3.78541
    return g
def mostrar_resultados(g):
    print("litros a galones es "+ str(g))




#*** codigo principal ***
litros = pedir_litros()
g = hacer_calculo(litros)
mostrar_resultados(g)
