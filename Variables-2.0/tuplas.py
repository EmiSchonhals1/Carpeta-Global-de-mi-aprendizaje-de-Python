#DIFERENTES FORMAS DE CREAR TUPLAS

#forma normal
tupla = ("Dato 1", "Dato 2")

#creando tuplas con tuple() (SOLO RECIBE COMO PARÁMETRO UNA LISTA)
tupla_funcion = tuple(["Dato 1", "Dato 2"]) #le pasamos una lista y la transforma en tupla

#creando una tupla sin paréntesis de multiples datos
tupla_multiple = "Dato 1","Dato2"

#creando una tupla sin paréntesis de un solo dato
tupla_sola = "Dato ",  #si es un solo dato debemos poner la coma (,) al final ya que sino lo tomara como un string común y corriente


#Las tuplas debemos crearlas cuando son datos de SOLO LECTURA, ya que la tupla es inmutable y no puede modificarse
