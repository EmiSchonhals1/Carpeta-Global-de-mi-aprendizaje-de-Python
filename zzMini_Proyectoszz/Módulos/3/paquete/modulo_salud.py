
def imc (peso,altura) :
    #cálculo del Índice de Masa Corporal
    imc = (peso / (altura)**2)
    
    if (imc < 18.5) :
        resultado = "Su peso es inferior al normal"
        #print ("Su peso es inferior al normal")
    elif (imc >= 18.5 and imc <= 24.9) :
         resultado = "Peso normal"
         #print ("Peso normal")
    elif (imc >= 25 and imc <= 29.9) :
        resultado = "Peso superior al normal"
        #print ("Peso superior al normal")
    elif (imc >= 30) :
        resultado = "Obesidad"
        #print ("Obesidad")
        
    return resultado
#SI NO DEVOLVIERAMOS EL RESULTADO CON UN RETURN Y USARAMOS PRINT NOS DEVOLVERIA NONE AL FINAL DEL RESULTADO

