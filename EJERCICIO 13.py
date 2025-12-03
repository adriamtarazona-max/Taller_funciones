#*** zona funcion ***
def pedir_lbase():
    lbase=int(input("Digite la longitud de la base:"))
    return lbase
def pedir_ancho():
    c=int(input("Dgite el ancho de la base:"))
    return c
def pedir_altura():
    h=int(input("Dgite el altura de la base:"))
    return h
def hacer_calculo(lbase,c,h):
    v= (lbase * h * c)/3
    return v
def mostrar_resultado(v):
    print("el volumen de la pramide es"+str(v))



#*** codigo principal ***
lbase= pedir_lbase()
c = pedir_ancho()
h = pedir_altura ()
v =  hacer_calculo(lbase,c,h)
mostrar_resultado(v)
