"""Librería Random de Python"""
import random as r

#print(dir(r)) #Se muestran las funciones dentro de esta librería

#print (r.randint(1 , 100)) #Metodo randint para generar un número aleatorio

random_number = r.randint(1 , 100) #Declarar una variable que guarde el numero aleatorio

print (random_number)

player = input("Ingresa un número aleatorio entre el 1 y 100: ") #Función input para que la usuaria escriba un número

print(player) #Se imprime el numero que haya ingresado la usuaria
