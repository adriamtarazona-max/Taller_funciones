#**** zona funcion ****
def pedir_datos():
    longitud= float(input("Digite la longitud del prisma rectangular:"))
    ancho= float(input("Digite el ancho del prisma rectangular:"))
    altura= float(input("Digite la altura del prisma rectangular:"))
    return longitud, ancho, altura
def volumen_prisma(longitud, ancho, altura):
    return longitud * ancho * altura
def mostrar_resultados(volumen):
    print("el volumen del prisma rectangular es"+ str(volumen))



#**** codigo principal ****
longitud, ancho, altura= pedir_datos()
volumen= volumen_prisma(longitud, ancho, altura)
resultado= mostrar_resultados(volumen)