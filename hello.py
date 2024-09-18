"""Este es un comentario de tipo DocString: Este módulo (archivo) contiene la práctica de crear 
    string en archivos de tipo Python
"""
# Esta es otra forma de hacer comentarios

MSG = "Hola Susy"  #Las variables que son constantes deben ir en mayúsculas

print(MSG)

print(MSG + " Hola Flor")

def saludar():  # Funcion en python se declara con la sentencia def
    """ Imprimir la variable msg concatenando un string"""
    print (MSG + " ¿cómo estás?")

    #return saludar() No es necesario porque está solo está devolviendo la función, podría solo
    #llamar a la función para que se ejecute
saludar()
