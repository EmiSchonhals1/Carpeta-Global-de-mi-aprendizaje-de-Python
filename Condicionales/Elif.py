ingreso_mensual = 10000

if ingreso_mensual >= 100000 :
    print ("Sos millonario")
elif ingreso_mensual >= 50000 :  #USAMOS ELIF (unión de else if) PARA CONDICIONALES ANIDADOS
    print ("Tenes buena money")
elif ingreso_mensual >= 9000 :   #LOS ELIF JAMÁS PUEDAN IR DSP DE UN ELSE, SOLO DSP DE UN IF
    print ("Sos clase media")
else: print ("Sos pobre")        #EN ESTE CASO USAMOS SOLO ELSE YA QUE ACCIONA SI NO SE CUMPLE NINGUNA OTRA CONDICIÓN