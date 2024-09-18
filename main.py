"""Traer la variable que está dentro del módulo hello"""
from hello import MSG  #Una manera de importar el contenido del módulo hello
import hello as hi  #Segunda manera de importar hello renombrandolo, lo trae el como objeto

print (MSG)
print ("Hola Mundo")

print(hi.saludar)
