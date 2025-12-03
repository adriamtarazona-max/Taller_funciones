#*** zona funcion ***
def pedir_kilometros():
    k=int(input("digite cuantos kilometros va a pasar a millas:"))
    return k
def hacer_calculo(k):
    t=0.621371 * k
    return t
def mostrar_resultado(t):
    print("kilometros a millas es"+ str(t))




#**** cogido principal ****
k=pedir_kilometros()
t=hacer_calculo(k)
mostrar_resultado(t)

