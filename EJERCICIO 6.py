#*** codigo funcion ***
def pedir_radio():
    radio = float(input("digite el radio del cono"))
    return radio
def pedir_altura():
    altura = float(input("digite la altura del cono"))
    return altura
def definir_pi():
    black= float(3.14)
    return black
def calcular_volu(radio, altura, black):
    vol = 0.33 * black * ( radio **2) * altura
    return vol
def mostrar_datos(radio, altura):
    mensaje= " el radio del cono es:"+ radio
    mensaje = "la altura del como es:"+ altura

def mostrar_resultado(resulatdo_vol):
    print("el volumen del cono es"+ str(resulatdo_vol))
    
#** codigo principal **
radio = pedir_radio()
altura = pedir_altura()
vol = calcular_volu(radio, altura, black=3.14)
resultado = mostrar_resultado(vol)

    