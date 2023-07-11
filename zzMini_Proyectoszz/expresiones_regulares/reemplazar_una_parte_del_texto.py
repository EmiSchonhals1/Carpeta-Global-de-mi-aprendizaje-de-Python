#Reemplazaremos una parte del texto por lo que nosotros querramos

#importamos la libreria re
import re

texto = "La fecha es 18/04/2023 y está lloviendo"

#patron que deseamos buscar y reemplazar
patron = r"\d{2}/\d{2}/\d{4}"

reemplazo = "Fecha oculta"

#sub encuentra la cadena especificada y la reemplaza por otra en el texto seleccionado
new_text = re.sub(patron, reemplazo, texto)

#mostramos el texto modificado
print(f"El texto modificado es: {new_text}")

