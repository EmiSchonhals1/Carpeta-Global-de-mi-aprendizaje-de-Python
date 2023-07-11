#Algoritmo que emula el ingreso a una red social con previa creación de cuenta, en caso de que ingresemos
#la contraseña de forma errónea nos debe preguntar si queremos cambiarla (en ese caso actualiza la contraseña y 
# vuelve a pedir datos), en cambio si volvemos a ingresar el usuario de forma errónea nos debe cerrar el programa con 
# un mensaje alusivo, y si ingresamos bien todos los datos un mensaje alusivo de bienvenida
 

#Cuenta creada con anterioridad
user_creado = "EmiSchonhals"
pass_creado = "Emiliano10"

intentos = int(0)

#Validando si los datos ingresados son iguales a los de la cuenta previamente creada
username = input("Ingrese su nombre de usuario: ")
if (username == user_creado) :
    print ("Usuario correcto")
    print ("----------------------------------------------------------------------------")
    password = (input("Ingrese su contraseña: "))
    
    while (password != pass_creado) :
        password = input ("Contraseña incorrecta, por favor vuelva a ingresarla: ")
        intentos = intentos + 1
        if (intentos >= 3) :
            opcion = input ("Desea cambiar su contraseña: ingrese 1 (sí) o 2 (no): ")
            if (opcion == "1") :
                contraseña_actualizada = input ("Ingrese su nueva contraseña: ")
                print ("------------------------------------------------------------------------")
                print ("Contraseña actualizada correctamente")
                print ("------------------------------------------------------------------------")
                break
            elif (opcion == "2") : 
                print ("------------------------------------------------------------------------")
                print ("Como ocurrió un error en la cuenta le pedimos que vuelva a intentarlo en otro momento")
                print ("------------------------------------------------------------------------")
                break
                
            
    if (password == pass_creado) :
     print ("------------------------------------------------------------------------")
     print (f"Bienvenido devuelta {username}")
     print ("------------------------------------------------------------------------")
else : 
 
 username_new = input ("Usuario incorrecto, por favor vuelva a ingresarlo: ")
 if (username_new != user_creado) :
     print ("------------------------------------------------------------------------")
     print ("Cuenta errónea, ingrese en otro momento")
     print ("------------------------------------------------------------------------")
 else: 
     if (username_new == user_creado) :
       print ("Usuario correcto")
       print ("----------------------------------------------------------------------------")
       password = (input("Ingrese su contraseña: "))
    
     while (password != pass_creado) :
        password = input ("Contraseña incorrecta, por favor vuelva a ingresarla: ")
        intentos = intentos + 1
        if (intentos >= 3) :
            opcion = input ("Desea cambiar su contraseña: ingrese 1 (sí) o 2 (no): ")
            if (opcion == "1") :
                contraseña_actualizada = input ("Ingrese su nueva contraseña: ")
                print ("------------------------------------------------------------------------")
                print ("Contraseña actualizada correctamente")
                print ("------------------------------------------------------------------------")
                break
            elif (opcion == "2") : 
                print ("------------------------------------------------------------------------")
                print ("Como ocurrió un error en la cuenta le pedimos que vuelva a intentarlo en otro momento")
                print ("------------------------------------------------------------------------")
                break
                
            
     if (password == pass_creado) :
      print ("------------------------------------------------------------------------")
      print (f"Bienvenido devuelta {user_creado}")
      print ("------------------------------------------------------------------------") 
 
#FALTA CREAR UNA PREGUNTA DE SEGURIDAD EN EL CASO DE QUE LA PERSONA ACCEDA A MODIFICAR SU CONTRASEÑA,
#PARA EVITAR QUE LA MODIFIQUE UNA PERSONA EQUIVOCADA







    
    



















