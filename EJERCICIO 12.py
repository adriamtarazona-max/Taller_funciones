#*** zona funcion ***
def pedir_lado():
    l=int(input("Digite uno de los lados del cuadrado:"))
    return l
def hacer_calculo(l):
    a= l^2
    return a
def mostar_mensaje(a):
    print("el area del cuadrado es"+  str(a))



#*** codigo principal ***
l = pedir_lado()
a = hacer_calculo(l)
mostar_mensaje(a)
