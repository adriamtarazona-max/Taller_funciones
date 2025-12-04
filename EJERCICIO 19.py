#*** zona funcion ***
def pedir_datos():
    base =float(input("Digite la base del prisma triangular:"))
    altura = float (input("Digite la altura del prisma triangular:"))
    ancho = float(input("Digite el ancho del prisma triangular:"))
    return base, altura, ancho
def hacer_calculo(base, altura,ancho):
    v= (base * altura * ancho)/3
    return v
def mostrar_resultados(v):
    print("El volumen del prisma triangular es"+ str(v))



#*** codigo principal ***
base, altura, ancho = pedir_datos()
v = hacer_calculo(base, altura, ancho)
mostrar_resultados(v)
    