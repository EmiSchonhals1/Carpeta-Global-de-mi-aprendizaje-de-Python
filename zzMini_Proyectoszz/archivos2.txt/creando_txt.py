#Creamos el archivo.txt de nombres y edades para luego ordenar por edades

#Como el archivo.txt no existe aún, lo abrimos como WRITE, total no nos interesa que se borren los datps anteriores x q no hay nada
with open("zzMini_Proyectoszz\\archivos2.txt\\archivo_personas.txt", "w", encoding="UTF-8") as archivo :
    nombre = []
    edad = []
    cant_personas = 4
    lista = []
    for i in range(cant_personas) :
        persona = input("Ingrese nombre: ")
        años = int(input("Ingrese edad: "))
        archivo.write(f"{persona} \n")
        archivo.write(f"{años} \n")

        
    
   
