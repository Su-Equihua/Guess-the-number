"""Librería Random de Python"""
import random as r
import time

MIN_NUMBER = 1
MAX_NUMBER = 100

# Función para volver a jugar
def start_game_again(game_function):
    play_again = input("\n¿Quieres volver a jugar? (Si o No): ")
    while play_again.lower() not in ("si" , "no"):
        print ("\n Por favor ingresa una respuesta válida (Si o No)")
        play_again = input("\n¿Quieres volver a jugar? (Si o No): ")

    if play_again.lower() == "si":
        print ("¡Vamos a jugar de nuevo!")
        game_function()   #Inicia el juego otra vez
    else:
        print("\n ¡Gracias por jugar!")

#Función para que el sistema cree un número aleatorio
def generate_random_number():
    return r.randint(MIN_NUMBER , MAX_NUMBER)

#Función para el turno de la jugadora
def get_player_number():
    # Manejo de excepciones
    try:
        player_number = int(input("Elige un número entero entre el 1 y 100: "))
        if MIN_NUMBER <= player_number <= MAX_NUMBER:
            return  player_number
        else:
            print  ("Recuerda, debe ser un número entre 1 y 100.\nInténtalo en tu siguiente turno")
            return None
    except ValueError: #No se recibió un número entero
        print("Recuerda debe ser un NÚMERO entero. Inténtalo otra vez")
        return None

#Función para obtener el numero del ordenador
def generate_computer_number():
    computer_player_number = r.randint(1 , 100)
    print ("La computadora ha elegido el número: " + str(computer_player_number))
    return computer_player_number

#Función para comparar los numeros de los jugadores con el numero adivinar
def compare_number(player_number, guess_number):
    if player_number > guess_number:
        return "El numero es menor, vuelve a intentarlo"
    elif player_number < guess_number:
        return "El numero es mayor, vuelve a intentarlo"
    return "\n---¡Felicidades, adivinaste el número correcto!---"

#Función para guardar el nombre de la jugadora
def get_player_name(name):
    name = input("\nAntes de comenzar, ¿cuál es tu nombre?: ")
    print (f"\n¡Hola {name}! Tu tendrás el primer turno")
    return name

#Función de la secuencia del juego
def guess_the_number():
    print("\n---¡Bienvenid@ a Guess The Number!--- \nUn juego en el que tú y la computadora intentarán adivinar un número secreto.")
    time.sleep(1)
    player_name = get_player_name("name")
    time.sleep(.8)
    print("Estamos creando el número secreto...")
    time.sleep(1.5)

    secret_number = generate_random_number()
    print (f"Número a adivinar: {secret_number}")
    
    turn = "Jugadora"
    player_assumptions = []
    computer_assumptions = []

    game_over = False

    while not game_over:
        if turn == "Jugadora":       
            print(f"\n---Round: {player_name}---")
            player_number = get_player_number()
            player_assumptions.append(player_number)
            print (f"Números intentados por {player_name}: {player_assumptions}")            
            compare_result = compare_number(player_number, secret_number)
            print(compare_result)

            if compare_result == "\n---¡Felicidades, adivinaste el número correcto!---":
                print (f"\n---¡Felicidades, {player_name} has ganado!---")
                game_over = True
                start_game_again(guess_the_number)
                time.sleep(.9)
                break

            turn = "Computadora"
            time.sleep(.8)

        else:
            print(f"---Round:{turn}---")
            player_number = generate_computer_number()
            computer_assumptions.append(player_number)
            print(f"Numeros intentados por la computadora: {computer_assumptions}")
            compare_result = compare_number(player_number, secret_number)
            print(compare_result)

            if compare_result == "\n---¡Felicidades, adivinaste el número correcto!---": 
                print ("\n---¡La computadora ha ganado!---")
                game_over = True
                start_game_again(guess_the_number)
                time.sleep(.8)
                break

            turn = "Jugadora"

guess_the_number()

# generate_random_number()
# get_girlplayer_number()
# generate_computer_number()
# comparison_number(36 , 36)
# girlplayer_name("name")
# start_game_again(guess_the_number)
