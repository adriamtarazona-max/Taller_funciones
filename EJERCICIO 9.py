#*** zona funcion ***
def leer_datos():
    base_mayor = float(input("Digite  la base mayor del trapecio:"))
    base_menor = float(input("Digite la base menor del trapecio:"))
    altura = float(input("Digite la altura del trapecio:"))
    return base_mayor, base_menor, altura
def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor)) / 2 * altura
def imprimir_resultado(area):
    print("el area del trapecio es"+ str(area))

   
#**** codigo rincipal ****
base_mayor, base_menor , altura= leer_datos()
area=area_trapecio(base_mayor, base_menor, altura)
imprimir_resultado(area)

