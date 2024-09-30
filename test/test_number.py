import unittest  #Importar el módulo test de python
from main import generate_random_number, MIN_NUMBER, MAX_NUMBER, compare_number, get_player_number
from unittest.mock import patch #Para simular una respuesta en el test


#Definir una clase de prueba que hereda de unittest.TestCase
class TestGuessTheNumber(unittest.TestCase):   #Se escribe en CamelCase = PascaleCase

#---------Test para probar que se genera un numero en el rango 1-100---------
    def test_generate_random_number(self):     #La palabra test le indica al ejecutor de pruebas que métodos representan pruebas
        result = generate_random_number()
        self.assertGreaterEqual(result, MIN_NUMBER)
        self.assertLessEqual(result, MAX_NUMBER)

#---------Test para validar la entrada del usario---------
    #Simular el valor de la función input. Target: Es el objetivo a simular (builtins.input)
    #Reempplazar la entrada de la jugadora por un objeto simulado durante la ejecución de la prueba
    @patch('builtins.input', side_effect=['3.14', '50'])  # Simular que primero ingresa un número negativo y luego uno válido
    @patch('builtins.print')  # Simular la función print
    def test_player_number_float(self, mock_print, mock_input):
        result = get_player_number()
        # Verificar que se imprime el mensaje de error para un número con decimal
        mock_print.assert_called_with("Entrada no válida. Debe ser un NÚMERO entero. Inténtalo otra vez.")        
        # Verificar que el número válido se devuelve correctamente
        self.assertEqual(result, 50)

    @patch('builtins.input', side_effect=['60'])
    def test_valid_player_number(self, mock_input):
        result = get_player_number()
        self.assertEqual(result, 60)

    @patch('builtins.input', side_effect=['abc', '150', '75'])
    def test_invalid_then_valid_player_number(self, mock_input):
        result = get_player_number()
        self.assertEqual(result, 75)

#----------Test para comparar los numeros de los jugadores con el número del juego ----------
    def test_compare_number_higher(self): #El número es mayor
        result_higher = compare_number(player_number=60, guess_number=50)
        self.assertEqual(result_higher, "El numero es menor, vuelve a intentarlo")
    
    def test_compare_number_lower(self): #El numero es menor
        result_lower = compare_number(player_number=40, guess_number=50)
        self.assertEqual(result_lower, "El numero es mayor, vuelve a intentarlo")
    
    def test_compare_number_correct(self): #Números iguales
        result_equal = compare_number(player_number=50, guess_number=50)
        self.assertEqual(result_equal, "\n---¡Felicidades, adivinaste el número correcto!---")

#Punto de entrada para ejecutar las pruebas
if __name__ == '__main__':    #Bloque para ejecutar las pruebas
    unittest.main()       #Proporciona una interfaz de línea de órdenes para el script de prueba
