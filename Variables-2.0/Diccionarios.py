#Formas de crear Diccionarios 

#Forma normal
#diccionario = {
#    'nombre'  "Emiliano",
 #   'Apellido' : "Schonhals" ,
  #  'edad' : 19
#}

#Función dict 
diccionario2 = dict(nombre="Emiliano", apellido="Schonhals", edad=19)  #Nos permite crear diccionarios vacíos

#Crear diccionarios con todos valores indefinidos
diccionario3 = dict.fromkeys(["nombre", "apellido", "edad"])

#Crear diccionarios en los q todos los elementos tengan el valor que deseemos
diccionario4 = dict.fromkeys(["nombre", "apellido", "edad"], "Bokita papá")

#Crear diccionarios que a cada caractér le de valores indefinidos
diccionario5 = dict.fromkeys("ABCDE")

#Crear diccionarios que a cada caracter le de un valor elegido
diccionario6 = dict.fromkeys("ABCDE", 5)

print (diccionario4)








