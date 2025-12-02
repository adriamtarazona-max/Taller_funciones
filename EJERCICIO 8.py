#*** zona de funcion ***
def pedir_dolares():
    dolares = float(input("digite cantidad de dolares que desea convertir:"))
    return dolares
def dar_tasa():
    tasa_cambio = 0.85
    return tasa_cambio
def convertir_dolares_euros(dolares, tasa_cambio):
    euros = dolares * tasa_cambio
    return euros
def mostrar_resultado(resultado_euros):
    print(f"{dolares} dolares equivalen a {euros} euros con una tasa de cambio")

#*** codigo principal ***
dolares = pedir_dolares()
tasa_cambio =dar_tasa()
euros =convertir_dolares_euros(dolares, tasa_cambio)
resultado = mostrar_resultado(euros)

