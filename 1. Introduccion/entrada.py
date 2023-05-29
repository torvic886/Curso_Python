nombre_completo = input('Ingrese su nombre Completo: ');

edad = input('Ingresa tu edad: ')
edad = int(edad) #casteo

altura = float(input('Ingresa tu altura: '))
# altura = float(altura)

autorizacion = input('¿ Autorizas el programa? (si/no)')
autorizacion = autorizacion == 'si'


print(nombre_completo)
print('Tipo de dato nombre_completo: ',type(nombre_completo))
print(edad)
print('Tipo de dato edad: ',type(edad))
print(altura)
print('Tipo de dato altura: ',type(altura))
print(autorizacion)