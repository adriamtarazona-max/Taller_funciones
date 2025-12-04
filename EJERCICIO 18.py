#*** zona funcion ***
def pedir_datos():
    lado = float(input("Digite el lado del  haxagono reagular:"))
    base = float(input("Digite la base del hexagono regular:"))
    altura = float (input("Digite la altura del hexagono regular:"))
    return lado, base, altura
def hacer_calculo(lado, base, altura):
    return (base * lado ) /2 * altura
def mostrar_resultado(area):
    print("el area del hexagono regular es "+ str(area))



#**** codigo principal ****
lado, base, altura = pedir_datos()
area = hacer_calculo(lado, base, altura)
mostrar_resultado(area)
    