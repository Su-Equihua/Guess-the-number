"""Librería Random de Python"""
import random as r
import time

#Función de control de turnos del juego

def guess_the_number():
    #Bienvenida al juego
    print("\n----¡Bienvenida a Guess The Number!---- \nVeremos quién adivina primero el número secreto")
    print("Creando el número secreto...")
    time.sleep(2)

    random_number = r.randint(1 , 100) #Numero a adivinar
    print (f"Número a adivinar es: {random_number}")

    turn = "Jugadora" #Inicia el juego con la jugadora

    while True: #La sentencia funciona para alternar los turnos del juego

        if turn == "Jugadora":
            print (f"\n----Round:{turn}----")
            girlplayer_number = int(input("Ingresa un número entero entre el 1 y 100: "))
         
            if 1 <= girlplayer_number <= 100:  #Verificar que se encuentre dentro del rango
                if girlplayer_number > random_number:
                    print ("El número es menor, vuelve a intentarlo")
                elif girlplayer_number < random_number:
                    print ("El numero es mayor, vuelve a intentarlo")
                else:
                    print("¡Felicidades, adivinaste el número correcto!")
                    print("Computadora, tu has perdido")
                    start_game_again(guess_the_number)
                    break #Termina el juego
            else:
                print  ("Recuerda debe ser un número entre 1 y 100")
            
            turn = "Computadora"
            time.sleep(1.5)

        else: #Turno de la computadora
            print (f"\n----Round:{turn}----")
            computer_player_number = r.randint(1 , 100)
            print ("La computadora ha elegido el número: " + str(computer_player_number))

            if computer_player_number < random_number:
                print ("El numero es mayor, vuelve a intentarlo")
            elif computer_player_number > random_number:
                print ("El numero es menor, vuelve a intentarlo")
            else:
                print ("¡Felicidades, adivinaste el número correcto!")
                print("Jugadora, tu has perdido")
                start_game_again(guess_the_number)
                break
                
            turn = "Jugadora"
            time.sleep(1.5)

guess_the_number()
