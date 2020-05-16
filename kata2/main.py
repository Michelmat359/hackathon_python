'''
Una panaderia vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribe un programa que comience leyendo el numero de barras vendidas que no son del dia. 
Despus tu porgrama debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. 
'''

precio = 3.49
precioDescuento = 3.49*0.40

barrasdepan = input('¿Cuantas barras de pan hay vendidas? ')

print ('Precio habitual: ' + str(precio))
print ('Descuento: ' + str(round(precioDescuento,2)))
print('El precio final es ' + str(round(precioDescuento * float(barrasdepan), 2)))