#Leeremos línea por línea los jugadores de Boca---------------------------------------------------------

#Abrimos el Archivo
archivo = open("zzMini_Proyectoszz\\archivos.txt\\formacion_boca.txt", encoding="UTF-8")

#Leemos el Archivo creando un array línea por línea----------------------------------------------------
lineas = archivo.readlines()

#almacenamos la información que necesitamos------------------------------------------------------------
arquero = lineas[1]
defensores = lineas[2]
mediocampistas_defensivos = lineas[3]
mediocampistas_ofensivos = lineas[4]
delanteros = lineas[5]
suplentes = lineas[6]

#Cerramos el archivo-----------------------------------------------------------------------------------
archivo.close()


#Printeamos los resultados
print (f"""        ARQ: {arquero}
        DEF: {defensores}
        MCD: {mediocampistas_defensivos}
        MCO: {mediocampistas_ofensivos}
        DEL: {delanteros}
        SUPLENTES: {suplentes}""")



