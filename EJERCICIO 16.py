#*** zona funcion ***
def pedir_lado():
    lado = float(input("Digite la longitud del lado del cubo:"))
    return lado
def cacular_volumen(lado):
    volumen = lado ** 3
    return volumen
def mostrar_resultado(volumen):
    print("el volumen del cubo es:"+ str(volumen))


#*** codigo principal ***
lado = pedir_lado()
volumen = cacular_volumen(lado)
mostrar_resultado(volumen)
