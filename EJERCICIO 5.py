#*** zona de funcion ***
def dar_radio():
    radio = 10
    return radio
def dar_pi():
    pi = 3.14
    return pi
def calcular_area(pi,radio):
    area = pi * (radio **2)
    return area
def mostrar_dato(pi, radio):
    mensaje = " El resultado de pi es:"+ pi
    mensaje = " El radio del circulo es:"+ radio
    
def mostrar_resultado(resulatdo_area):
    print("el area del circulo es:"+ str (resulatdo_area))


#*** codigo principal ***
radio = dar_radio()
pi = dar_pi()
area = calcular_area(pi, radio)
resultado = mostrar_resultado(area)
