#*** zona fumcion ***
def pedir_radio():
    radio = float(input("Digite el radio del circulo:"))
    return radio
def hacer_calculo(radio):
    circunferencia = 2 * 3.1416 * radio
    return circunferencia
def mostrar_resultado(circunferencia):
    print("la circunferencia del circulo es:"+ str(circunferencia))





#*** codigo principal ***
radio = pedir_radio()
circunferencia = hacer_calculo(radio)
mostrar_resultado(circunferencia)
