#*** zona funcion ***
def pedir_kilometros():
    km= float(input("Digite la distancia de los kilometros:"))
    return km
def hacer_calculo(km):
    millas= km * 0.621371
    return millas
def mostrar_resultado(millas):
    print ("Las milas a kilometros es:"+ str (millas))



#*** codigo principal ***
km = pedir_kilometros()
millas = hacer_calculo(km)
mostrar_resultado(millas)
