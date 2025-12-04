#*** zona funcion ***
def pedir_numero():
    numero = int(input("Digite numero:"))
    return numero
def vaidar_numero(dato_numero):
    if dato_numero %  2 == 0:
        mensaje = "el numero es par"
    else:
        mensaje = "El numero impar es"
    return mensaje

def mostrar_resultado (dato_mensaje):
    print("El numero es: " + dato_mensaje) 



#*** codigo principal ***
dato_numero = pedir_numero()
dato_mensaje = vaidar_numero(dato_numero)
mostrar_resultado(dato_mensaje)
