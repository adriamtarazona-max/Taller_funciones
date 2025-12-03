#*** zona funcion ***
def pedir_datos():
    base = float(input("Digite la base del paralelograma:"))
    altura = float(input("Digite la altura del paralelograma"))
    return base, altura
def hacer_calculo(base, altura):
    area= base * altura
    return area
def mostrar_resultados(area):
    print("el area del paralelograma es"+ str(area))



#*** codigo principal ***
base, altura = pedir_datos()
area = hacer_calculo(base,altura)
mostrar_resultados(area)
