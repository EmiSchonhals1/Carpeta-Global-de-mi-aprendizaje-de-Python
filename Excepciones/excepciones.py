
def sumar_dos() :
    #usamos el bucle while con la condición True para que no termine de ejecutarse hasta que se ingresen bien los datos
    while True :
        num1 = input("número 1: ")
        num2 = input("número 2: ")
        #ponemos try donde pudiera existir alguna excepcion, en este caso por un dato mal ingresado del usuario
        try :
            resultado = int(num1) + int(num2)
            #si no ocurren excepciones salimos del bucle while
            break 
        #si la excepción ocurre mostramos el texto en pantalla y se repetirá el bucle while hasta que ingrese bien los datos
        except :
            print("Te pedi un entero, volvé a ingresar los datos")
    
    #una vez salga del bucle while teniendo los datos correctos se devuelve el resultado
    return resultado
    

print("Inicio del programa")
print("Ingrese dos números para sumarlos")
#llamada y muestra de la función, en este caso no le pasamos parámetros ya que ingresamos los datos dentro de la misma
print(sumar_dos())






