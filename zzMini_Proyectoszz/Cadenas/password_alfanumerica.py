#emulador de contraseña alfanumérica

password = input("Ingrese una contraseña alfanumérica: ")

resultado = password.isalpha()

if (resultado == False) :
    print ("Contraseña almacenada correctamente")
else : 
    print ("La contraseña no es alfanumérica, por favor vuelva a ingresarla")
    print ("---------------------------------------------------------------")
    
    resultado = True
    while (resultado == True) :
        password_new = input("Ingrese otra contraseña: ")
        resultado_new = password_new.isalpha()
        if (resultado_new == False) :
            print("Ahora si es alfanumérica")
            break
