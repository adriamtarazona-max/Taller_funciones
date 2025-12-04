#*** zona funcion ***
def pedir_datos():
    horas = float(input("Digite el numero de horas:"))
    return horas
def hacer_calculo(horas):
    minutos = horas * 60
    return minutos
def mostar_resultado(minutos):
    print("horas a minutos es"+ str(minutos))


 
#*** codigo principal ***
horas = pedir_datos()
minutos = hacer_calculo(horas)
mostar_resultado(minutos)
