"""Librería Random de Python"""
import random as r

#print(dir(r)) #Se muestran las funciones dentro de esta librería
#print (r.randint(1 , 100)) #Metodo randint para generar un número aleatorio
#random_number = r.randint(1 , 100) #Declarar una variable que guarde el numero aleatorio
#print (random_number)


random_number = r.randint(1 , 100)
#print (f"Número a adivinar: {random_number}")

girlplayer_number = int(input("Ingresa un número aleatorio entre el 1 y 100: "))
    # int( ) para convertir el valor de input en numero
#print (girlplayer_number)

computer_player_number = r.randint(1 , 100)
#print ("Numpero del jugador computadora: " + str(computer_player_number))

#Función principal para el control del juego
def guess_the_number():
    #Bienvenida al juego
    print("Bienvenidos a Guess The Number\nAdivina el número al azar que ha creado el ordenador")
    
    turno = "jugador"  #Variable para indicar de quién es el turno
    NUMBER = random_number
    while True:  #Mientras la expresión sea verdadera
       if turno == girlplayer_number:  
            if girlplayer_number > random_number:
                print (int(input("El número es menor: ")))

guess_the_number()
