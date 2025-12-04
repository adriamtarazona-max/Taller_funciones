#*** zona fucion *** 
def definir_datos():
    longitud = float(input("Digite la longitud del rectangulo:"))
    ancho = float(input("Digite el ancho de rectangulo:"))
    return longitud, ancho
def hacer_calculo(longitud, ancho):
    area = longitud * ancho 
    return area
def mostrar_resultado(area):
    print("El area del rectangulo es:" + str(area))




#*** codigo principal ***
longitud, ancho = definir_datos()
area = hacer_calculo(longitud, ancho) 
mostrar_resultado(area)  
