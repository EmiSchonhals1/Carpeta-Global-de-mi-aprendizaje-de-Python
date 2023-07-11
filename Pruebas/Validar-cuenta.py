username_guardado = "Elias"
password_guardado = "12345"

username_ingresado = input("Ingrese su usuario: ")

if username_ingresado == username_guardado :
    print ("Usuario correcto, por favor ingrese la contraseña")
    password_2 = input("Ingrese su contraseña: ")
    if password_2 == password_guardado :
        print ("Acceso concedido, iniciando sesión")
    else : print ("Contraseña incorrecta, por favor vuelva a ingresarla")
else : print ("Usuario incorrecto, por favor vuelva a ingresar el usuario")        
    


