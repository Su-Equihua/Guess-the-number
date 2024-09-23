"""Librería Random de Python"""
import random as r

#print(dir(r)) #Se muestran las funciones dentro de esta librería
#print (r.randint(1 , 100)) #Metodo randint para generar un número aleatorio
#random_number = r.randint(1 , 100) #Declarar una variable que guarde el numero aleatorio
#print (random_number)

#Función principal para el control del juego
def guess_the_number():
    #Bienvenida al juego
    print("Bienvenidos a Guess The Number\nTu o la computadora adivinarán el número correcto")
    print("Creando el número secreto...")
    random_number = r.randint(1 , 100)
    print (f"Número a adivinar: {random_number}")
    girlplayer_number = int(input("Ingresa un número aleatorio entre el 1 y 100: "))
    # int( ) para convertir el valor de input en numero
    #print (girlplayer_number)

    #while girlplayer_number != random_number: #Mientras la expresión sea verdadera
    while True: #La sentencia puede funcionar tanto para el caso de la jugadora como de la computadora
        #if girlplayer_number is not None: #Sentencia no necesaria
        if 1 <= girlplayer_number <= 100: #Verificar que se encuentre dentro del rango
            if girlplayer_number > random_number:
                girlplayer_number = (int(input("El número es menor: ")))
            elif girlplayer_number < random_number:
                girlplayer_number = (int(input("El número es mayor: ")))
            else:
                print("¡Felicidades, adivinaste el número correcto!")
                break #Termina el juego
        else:
            girlplayer_number = int(input("Recuerda debe ser un número entre 1 y 100: "))

        computer_player_number = r.randint(1 , 100)
        print ("Ingresa un número aleatorio del 1 al 100: " + str(computer_player_number))
        if computer_player_number < random_number:
            pista = input("Dame una pista, el número es mayor o menor: ")
        if pista == "mayor":
            lower_bound = computer_player_number + 1
            computer_player_number = r.randint (lower_bound, 100)
        elif pista == "menor":
            upper_bound = computer_player_number - 1
            computer_player_number = r.randint(1 , upper_bound)
        else:
            print ("¡Felicidades, adivinaste el número correcto!")
        

guess_the_number()
