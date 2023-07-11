#PARÁMETRO *ARGS
def sumas (*numeros) : #con el asterisco definimos el parámetro como una lista, por lo tanto convierte todos los parámetros
                        #que le pasemos a un sólo parámetro
    numeros_sumados = 0 
    resultado = sum(numeros) #función que suma todos los valores
    return (resultado)

calculo = sumas(2,4,6,8)
print (calculo)

print ("---------------------------------------------------------------------------------------------------------------")

#si usamos el parámetro args junto con otros parámetros que no lo sean, siempre debemos ponerlo al final
#ya que sino no podremos agregar otro parámetro

def sumas (nombre,*numeros) : #con el asterisco definimos el parámetro como una lista, por lo tanto convierte todos los parámetros
                        #que le pasemos a un sólo parámetro
    numeros_sumados = 0 
    resultado = print (f"{nombre} la suma de tus números es igual a {sum(numeros)}")
    return (resultado)

calculo = sumas("Emiliano",2,4,6,8)
print (calculo)

print ("---------------------------------------------------------------------------------------------------------------")

#PARÁMETRO **KWARGS
def frase (nombre, apellido, adjetivo) :
    resultado = print (f"Hola {nombre} {apellido} sos muy {adjetivo}")
    return (resultado)

frase_resultante = frase(apellido = "Schonhals", adjetivo = "inteligente", nombre = "Emiliano")
#El orden en los que los definimos no afecta ya que son keywords arguments (**kwargs)
print (frase_resultante)

