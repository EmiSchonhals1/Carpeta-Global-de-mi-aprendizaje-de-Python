#FORMAS DE CREAR CONJUNTOS

#Forma normal
conjunto = {"Dato 1", "Dato 2"} 

#Función Set()
conjunto_set = set("Dato 1", "Dato 2")

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])  #crea un conjunto que puede ser congelado para que de esa forma sea hasheable (puede ser modificado)
conjunto2 = {conjunto1, "Dato 3"}
print (conjunto2)
