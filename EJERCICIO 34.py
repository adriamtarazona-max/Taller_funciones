#*** zona funcion ***
def pedir_datos():
    precio = float(input("Digite el precio del articulo:"))
    return precio
def hacer_calculo(precio):
    descuento = precio * 0.10
    return descuento
def mostrar_resultado(descuento):
    print("El descuento del articulo es:"+ str(descuento))
    
    
    
#*** codigo priincipal ***
precio = pedir_datos()
descuento = hacer_calculo(precio)
mostrar_resultado (descuento)
    