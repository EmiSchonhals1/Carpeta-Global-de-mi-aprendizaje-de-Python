#Algoritmo que calcula cuánto gana una persona por hora dependiendo de cuántas horas al día trabaja, cuántos días a 
#la semana trabaja y el pago del mes en total

horas_x_dia = int(input("Ingrese cuántas horas al día trabaja: "))
dias_x_semana = int(input("Ingrese cuántos dias a la semana trabaja: "))
pago_mensual = float(input("Ingrese el pago mensual: $"))
print ("-----------------------------------------------------------------")

pago_semanal = float(pago_mensual / 4)
pago_x_dia = float(pago_semanal / dias_x_semana)
pago_x_hora = float(pago_x_dia / horas_x_dia)

print (f"Su ganancia por hora es de ${pago_x_hora}")
print ("------------------------------------------------------------------")
