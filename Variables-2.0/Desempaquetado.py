#en este caso usamos una lista, tmb podemos usar tuplas o conjuntos
datos = ["Emiliano", "Schonhals", 19]
#desempaquetado (SIEMPRE DEBE HABER LA MISMA CANTIDAD DE VARIABLES QUE DE ELEMENTOS EN EL ARRAY)
nombre,apellido,edad = datos

#cada variable ya tomo el valor correspondiente, por ende ya podemos mostrar la que queramos
print (f"El nombre completo es {nombre} {apellido} y tiene {edad} años")
