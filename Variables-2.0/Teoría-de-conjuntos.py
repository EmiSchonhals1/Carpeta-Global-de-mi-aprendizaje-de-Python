conjunto1 = {1,2,3,4,5}
conjunto2 = {2,4}

#Saber si un conjunto es subconjunto de otro
resultado = conjunto2.issubset(conjunto1) #El método .issubset() nos permite saber si un conjunto es subconjunto de otro
#Nos devuelve True o False dependiendo si es subconjunto o no
print(resultado)


#Otra forma de saber si es un subconjunto
resultado2 = conjunto2 <= conjunto1
print (resultado2)



#Saber si un conjunto es superconjunto de otro
resultado3 = conjunto2.issuperset(conjunto1) #El método .issuperset() nos permite saber si un conjunto es superconjunto de otro
#Nos devuelve True o False dependiendo si es superconjunto o no
print (resultado3)

#Otra forma de saber si es un superconjunto
resultado4 = conjunto2 > conjunto1
print (resultado4)


#Saber si hay algún número en común
resultado5 = conjunto2.isdisjoint(conjunto1)  #El método .isdisjoint() sólo nos devolverá True si no hay ningun elemento que sea igual en ambos conjuntos, con que solo haya uno igual nos devolverá False
print (resultado5)