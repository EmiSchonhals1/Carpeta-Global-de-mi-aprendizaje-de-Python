
def imc (peso,altura) :
    #cálculo del Índice de Masa Corporal
    imc = (peso / (altura)**2)
    #Resultados
    if (imc < 18.5) :
        print ("Su peso es inferior al normal")
    elif (imc >= 18.5 and imc <= 24.9) :
        print ("Peso normal")
    elif (imc >= 25 and imc <= 29.9) :
        print ("Peso superior al normal")
    elif (imc >= 30) :
        print ("Obesidad")

