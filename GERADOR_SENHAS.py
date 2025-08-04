
# GERADOR DE SENHAS

from ASCII_Art import ascii_art
from OP import gerador




def menu(): # Menu de opções
     ascii_art()
     while True:
         
         print("*Gerar Senha*: 1")
         print("*Sair*: 0")
         escolha = input("Escolha uma opção: ")




         if escolha == "0":
             print("Saindo...")
             break



         if escolha == "1":
            print(gerador())




menu()