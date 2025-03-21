#En una empresa, los empleados trabajan en horario normal de 08:00 a.m. a 12:00 p.m. y de 02:00 p.m. a 06:00 p.m. 
#Sin embargo, algunos trabajadores trabajan horas nocturnas (después de las 06:00 p.m.), por las cuales tienen 
#derecho a una bonificación de $2.000 (dos mil pesos) por hora nocturna trabajada. Cree en Javascript un programa 
#que, primero pregunte al usuario si el trabajador ha trabajado horas nocturnas este mes, en caso de no haberlas 
#trabajado el programa debe mostrar el siguiente mensaje: “usted no tiene derecho a bonificación este mes”. 
#Si el trabajador ha trabajado horas nocturnas durante el mes, entonces el programa debe solicitar al usuario el 
#número de horas nocturnas trabajadas y luego mostrar un mensaje con el valor de la bonificación a la que tiene 
#derecho el trabajador, por ejemplo: “su bonificación este mes es de: 80000 pesos”

#primero pregunte al usuario si el trabajador ha trabajado horas nocturnas este mes
# NO: usted no tiene derecho a bonificación este mes
# SI: su bonificación este mes es de: 80000 pesos --bonificación de $2.000 (dos mil pesos) por hora nocturna trabajada.

afirmacion_nocturnas = input("Sr Usuario ha trabajo horas extras este mes?: ")
horas = int (input ("Horas Trabajadas: "))

print(f"su bonificación este mes es de: {(horas) * 2000}")  if (afirmacion_nocturnas.lower() == "si" and horas > 0) else print("usted no tiene derecho a bonificación este mes")