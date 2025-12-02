#*** codigo funcion ***
def dar_celsius():
    celsius =float(input("digite cuantos grados desea convrtir:"))
    return celsius
def calcular_faren(celsius):
    faren = celsius * 9/5 + 32
    return faren
def mostrar_datos(celsius):
    mensaje = "los grados celsius son:"
    
def mostrar_resultado(resultado_faren):
    print("la conversacion a grados fahrenheit dio =  "+ str(resultado_faren))
    
#*** codigo principal ***
celsius= dar_celsius()
faren = calcular_faren(celsius)
resultado = mostrar_resultado(faren)
