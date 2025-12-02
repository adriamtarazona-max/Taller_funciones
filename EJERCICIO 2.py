#*** zona funcion ***
def definir_radio():
    radio = 8
    return radio
def calcular_volumen(radio):
    vol= (4* 3.34 * 8)
    return vol 
def impirmir_datos(radio):
    mensaje= "el radio es:" + radio
    
def imprimir_mensaje(resultado):
    print("el volumen de la esfera es:"+ str(resultado))
    
    
#*** zona codigo principal ***
radio = definir_radio()
vol = calcular_volumen(radio)
reasultado = imprimir_mensaje(vol)
