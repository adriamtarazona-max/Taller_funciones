#*** zona funcion ***
def dar_altura():
    altura = 12
    return altura
def dar_base():
    base = 15
    return base
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area
def imprimir_datos(base, altura):
    mensaje= "la base es"+ base
    mensaje= "la altura es"+ altura
    
def imprimir_resultado(resultado_area):
    print("el area del triangulo es:" + str(resultado_area))


#*** codigo principal ***
base = dar_base()
altura = dar_altura()
area = calcular_area(base, altura)
resultado = imprimir_resultado(area)
