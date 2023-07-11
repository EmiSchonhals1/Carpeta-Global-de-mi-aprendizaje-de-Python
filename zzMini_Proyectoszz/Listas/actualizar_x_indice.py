lista = ["Jorge Lanata", 60, 1.67, "Periodista", "argentino"]
print (f"La lista es: {lista}")

continuar = "y"
    

opcion = input("Desea actualizar algún dato? y/n: ")
if (opcion == "y") :
    while (continuar == "y") :
        indice = int(input("Ingrese el índice que desea actualizar: "))
        elemento_actualizado = input("Ingrese el elemento que desea poner en su lugar: ")
        lista[indice] = elemento_actualizado
        
        print (f"La lista actualizada es: {lista}")
        continuar = input("Desea actualizar otro elemento? y/n: ")
    print ("Tenga buen día...")
elif (opcion == "n") :
    print ("Tenga un buen día...")
else : 
    print ("Opción incorrecta, vuelva a intentarlo en otro momento...")
