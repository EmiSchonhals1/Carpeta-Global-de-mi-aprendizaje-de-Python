
with open("zzMini_Proyectoszz\\Módulos+archivos.txt\\lista.txt", "w", encoding = "utf-8") as archivo :
    
    from modulo_sueldo import si_sueldo_es
    
    cant_personas = int(input("Ingrese la cantidad de personas censadas: "))
    lista = []
    
    archivo.write("LISTA DE PERSONAS CUYO SUELDO ES MAYOR O IGUAL A $700000 \n")
    for i in range(cant_personas) :
        sueldo = float(input("Sueldo: $"))
        nombre = input("Nombre: ")
       
        #llamada al módulo
        resultado = si_sueldo_es(sueldo,nombre)
        if (resultado == "si") :
            archivo.write(f"{nombre} ------ ${sueldo} \n")
            #SI O SI DEBE SER UN STRING, NO PODEMOS AGREGAR ITERABLES COMO LISTAS DE ESTA FORMA











