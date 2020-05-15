''' 
En bloque
'''
#Comentarios
nombre = 'Miguel Angel Mateo'
edad = 30
esta_trabajando = True;

dato = input('Introducir Dato: ')
print(dato)


if(edad >= 18):
    nombre2 = input('Tu nombre: ')
    print('Eres mayor de edad')
    print('Bienvenido ' + nombre + ' ' +nombre2)
else:
    print('Eres menor de edad')