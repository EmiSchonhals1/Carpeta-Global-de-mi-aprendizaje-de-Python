#Programa que accede a la línea del archivo que deseemos

#Abrimos de forma ÓPTIMA el archivo
with open("zzMini_Proyectoszz\\archivos.txt\\formacion_boca.txt", encoding="UTF-8") as archivo :
    
    #guardamos en un array el archivo línea por línea
    lista = archivo.readlines()
    
    
print("---------------------------------------------------------------------------------------------")
opcion = int(input("Ingrese lo que desea ver: 1(Arq), 2(Def), 3(Mcd), 4(Mco), 5(Del) o 6(Suplentes): "))

if (opcion == 1) :
    print(lista[1])
elif (opcion == 2) :
    print(lista[2])
elif (opcion == 3) :
    print(lista[3])
elif (opcion == 4) :
    print(lista[4])
elif (opcion == 5) :
    print(lista[5])
elif (opcion == 6) :
    print(lista[6])
else :
    print("Opción inválida")

