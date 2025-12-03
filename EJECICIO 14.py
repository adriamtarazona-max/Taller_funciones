#*** zona funcion ***
def pedir_pulgadas():
    p= int(input("Digite cuantas pulgadas va a pasar a centimetros:"))
    return p
def hacer_calculo(p):
    c= 2.54 * p
    return c
def mostrar_resultado(c):
    print("pulgadas a centietros es"+ str(c))




#*** codigo principal ***
p = pedir_pulgadas()
c = hacer_calculo(p)
mostrar_resultado(c)
