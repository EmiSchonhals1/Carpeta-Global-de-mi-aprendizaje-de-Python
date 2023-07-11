#PARTE A
#Promedios de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencias de duración
diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)  #restamos 100 a los cálculos del porcentaje para saber la DIFERENCIA
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max / 10) #------> en este caso usamos esta fórmula para que el resultado tenga solo un decimal
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)

print (f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rápido")
print (f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print (f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio")
print ("----------------------------------------------------------------------------------")


#PARTE B
#Calculando el porcentaje de tiempo vacío removido
crudo_promedio = 5
crudo_dalto= 3.5

tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio / 10)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío")
print(f"El curso de Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacío")
print ("----------------------------------------------------------------------------------")

#PARTE C
#Mostrando diferencias si los cursos duraran 10 horas
print (f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print (f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas del curso de Dalto")

























































