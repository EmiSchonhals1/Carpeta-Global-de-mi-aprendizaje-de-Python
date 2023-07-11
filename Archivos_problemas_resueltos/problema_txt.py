#Tenemos dos listas, una con nombres y otra con apellidos
#Debemos escribir los datos en un archivo de texto de forma óptima

nombres = ["Emiliano","José","Eric","Matías","Carmen"]
apellidos = ["Schonhals","Paradela","Schechtel","Abdala","García"]

#Creamos el archivo.txt con permiso de escritura
with open("Archivos_problemas_resueltos\\nombres_y_apellidos.txt", "w", encoding="utf-8") as archivo :
    archivo.writelines("LOS DATOS SON \n\n")
    for nom,ape in zip(nombres,apellidos) :
        archivo.writelines(f"Nombre: {nom} \nApellido: {ape} \n-------------------\n")



