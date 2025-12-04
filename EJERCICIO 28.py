#*** zona funcion ***
def pedir_datos():
    base = float(input("Digite la base del triangulo :"))
    altura = float(input("Digite la altura del traiangulo:"))
    return base, altura
def hacer_calculo(base, altura):
    area = base * altura /2
    return area
def mostrar_resultado(area):
    print("El area del triangulo es"+ str (area))


#*** codigo principal ***
base, altura = pedir_datos()
area = hacer_calculo(base, altura)
mostrar_resultado(area)
