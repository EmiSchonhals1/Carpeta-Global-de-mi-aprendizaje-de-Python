#Forma Simple
def saludar() :
    print ("Hola máquina, como andas?")

#llamando a la función creada
saludar()
print("--------------------------------------------------------------------------------------------------------")

#Creando una función con parámetros
def saludo(nombre,sexo) :
    sexo = sexo.lower() #pasamos sexo a minúsculas para su uso
    if (sexo == "mujer") :
        adjetivo = "reina"
        print (f"Hola {nombre}, mi {adjetivo}, como andas?")
    elif (sexo == "hombre") :
        adjetivo = "campeón"
        print (f"Hola {nombre}, mi {adjetivo}, como andas?")
 
        
#llamando a la funcion dependiendo lo que le pidamos
saludo("Emi","HOMBRE") #no importa como escribimos el sexo por que lo transformamos en minúsculas para su lectura
saludo("Brisa","MUjer")
print("--------------------------------------------------------------------------------------------------------")

#Creando una función que nos RETORNE UN VALOR
def sumando(num1,num2) :
    suma = num1 + num2
    return suma
    
#es necesario que una variable tome el valor retornado    
resultado = sumando(4,10)
print (f"El resultado de la suma es: {resultado}") 
print("--------------------------------------------------------------------------------------------------------")

#Creando función que nos RETORNE VARIOS VALORES
def sumando(num1,num2) :
    suma = num1 + num2
    return (suma,num1,num2)

#en este caso nos devuelve una tupla que podemos desempaquetar
resultado,nro1,nro2 = sumando(3,7)
print (f"Sumando los números {nro1} y {nro2} llegamos al {resultado}")




