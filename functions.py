"""Librería Random de Python"""
import random as r
import time

#Función para volver a jugar
def start_game_again(game_function):
    play_again = input("\n¿Quieres volver a jugar? (Si o No): ")
    while play_again.lower() not in ("si" , "no"): #Tupla (o lista) de respuestas
         print ("\n Por favor ingresa una respuesta válida (Si o No)")
         play_again = input("\n¿Quieres volver a jugar? (Si o No): ")

    if play_again.lower() == "si": #.lower() Es para que no sea sensible a mayusculas o minusculas
        print ("¡Vamos a jugar de nuevo!")
        game_function()   #Que inicie el juego otra vez
    else:
        print("\n ¡Gracias por jugar!")

#Función para que el sistema cree un número aleatorio
def generate_random_number():
    random_number = r.randint(1 , 100)
    print (f"Número a adivinar: {random_number}")
    return random_number

#Función para el turno de la jugadora
def get_girlplayer_number():
    # Manejo de excepciones
    try:
        girlplayer_number = int(input("Elige un número entero entre el 1 y 100: "))
        #int() Solo recibe numeros enteros
        if 1 <= girlplayer_number <= 100:  #Verificar que se encuentre dentro del rango
            return  girlplayer_number
        else:
            print  ("Recuerda debe ser un número entre 1 y 100.\nInténtalo en tu siguiente turno")
            return None
    except ValueError: # No se recibió un número entero
        print("Recuerda debe ser un NÚMERO entero. Inténtalo otra vez")
        return None

#Función para obtener el numero del ordenador
def generate_computer_number():
    computer_player_number = r.randint(1 , 100)
    print ("La computadora ha elegido el número: " + str(computer_player_number))
    return computer_player_number

#Función para comparar los numeros de los jugadores con el numero adivinar
def compare_number(player_number, guess_number1):
    if player_number > guess_number1:
        answer ="El numero es menor, vuelve a intentarlo"
    elif player_number < guess_number1:
        answer = "El numero es mayor, vuelve a intentarlo"
    else:
        answer = "\n---¡Felicidades, adivinaste el número correcto!---"
    print (answer)
    return answer

#Función para guardar el nombre de la jugadora
def girlplayer_name(name):
    name = input("\nJugadora ¿Cuál es tu nombre?: ")
    print (f"\n---¡Bienvenida {name}!---")
    return name



#Función de la secuencia del juego
def guess_the_number():
    print("\n---¡Bienvenida a Guess The Number!--- \nUn juego en el que tu y la computadora intentarán adivinar un número secreto.")
    player_name = girlplayer_name("name")
    print("Estamos creando el número secreto...")
    time.sleep(1.5) 

    secret_number = generate_random_number()
    
    turn = "Jugadora"
    girlplayer_assumptions = []
    computer_assumptions = []

    game_over = False

    while not game_over:
        if turn == "Jugadora":       
            print(f"\n---Round: {player_name}---")

            player_number = get_girlplayer_number()
            girlplayer_assumptions.append(player_number)
            print (f"Números intentados por {player_name}: {girlplayer_assumptions}")
            
            compare_result = compare_number(player_number, secret_number)
            if compare_result == "\n---¡Felicidades, adivinaste el número correcto!---":
                print (f"¡{player_name} ha ganado!")
                game_over = True
                start_game_again(guess_the_number)
                break

            turn = "Computadora"

        else:
            print(f"---Round:{turn}---")
            player_number = generate_computer_number()
            computer_assumptions.append(player_number)
            print(f"Numeros intentados por la computadora: {computer_assumptions}")
            compare_result = compare_number(player_number, secret_number)

            if compare_result == "\n---¡Felicidades, adivinaste el número correcto!---":
                print ("¡La computadora ha ganado!")
                game_over = True
                start_game_again(guess_the_number)
                break

            turn = "Jugadora"


guess_the_number()


# generate_random_number()
# get_girlplayer_number()
# generate_computer_number()
# comparison_number(36 , 36)
# girlplayer_name("name")
# start_game_again(guess_the_number)




