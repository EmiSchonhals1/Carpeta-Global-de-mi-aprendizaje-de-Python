
#AND (&)        #AMBAS CONDICIONES DEBEN SER TRUE
resultado = True & True     #Nos devolverá TRUE
resultado2 = True & False   #Nos devolverá FALSE
resultado3 = False & True   #Nos devolverá FALSE
resultado4 = False & False  #Nos devolverá FALSE

#OR (|)         #AMBAS CONDICIONES DEBEN SER FALSE
resultado5 =  True | True    #Nos devolverá TRUE
resultado6 =  True | False   #Nos devolverá TRUE
resultado7 =  False | True   #Nos devolverá TRUE
resultado8 =  False | False  #Nos devolverá FALSE

#NOT (not True o not False)    #NOS DEVUELVE LO CONTRARIO A LA CONDICION
resultado9 = not True    #Nos devuelve False
resultado10 = not False  #Nos devuelve True

print (resultado9)

