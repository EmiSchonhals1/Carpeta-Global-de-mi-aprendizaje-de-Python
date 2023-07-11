frutas = ["banana", "manzana", "naranja", "sandía"]

for i in frutas :
    #supongamos que no me gusta la manzana y deseo que no se muestre en pantalla al iterarse, deseo saltearla
    if (i == "manzana") :
        continue  #hace que salteemos el elemento, continuando asi el programa
    
    print (f"Me gusta la {i}")
