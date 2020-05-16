''' 
En bloque
'''


#Comentarios
nombre = 'Miguel Angel'
edad = 30
estaTrabajando = True

dato = input('Introducir Dato: ')
print(dato)


if(edad >= 18):
    nombre2 = input('Tu apellido: ')
    print('Eres mayor de edad')
    print('Bienvenido ' + nombre + ' ' +nombre2)
else:
    print('Eres menor de edad')