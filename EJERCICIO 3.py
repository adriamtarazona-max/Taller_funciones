#*** zona funcion ***
def dar_ancho():
    ancho = 16
    return ancho
def dar_longitud():
    longitud= 20
    return longitud
def calcular_area(ancho, longitud):
    area= (ancho * longitud)
    return area
def mostrar_dato(ancho, longitud):
    mensaje = "el ancho es:"+ ancho
    mensaje = "la longitud es:"+ longitud
    
def mostrar_resultado(resultado_area):
    print("el area del rectangulo es:"+ str(resultado_area))
    
    
#*** zona codigo principal ***
ancho = dar_ancho()
longitud = dar_longitud()
area = calcular_area(ancho, longitud)
resultado= mostrar_resultado(area)
