import random
import tkinter as tk
from tkinter import messagebox

palavras = ["chaves", "tabela", "cedula", "delete", "script"]

def jogo():

    print("ADIVINHE A PALAVRA!\nSUA PALAVRA TEM 6 LETRAS!")

    adivinhar = random.choice(palavras)

    tentativa = input()

    for i in list(adivinhar):

        for j in list(tentativa):

            certas = [elemento for elemento in adivinhar if elemento in tentativa]
    print(adivinhar)
    print(tentativa)
    print(certas)

def menu():

    print("======= BEM VINDO AO TERMO =======")
    print("======= ESCOLHA UMA OPÇÃO: =======")
    print("========== 1 - JOGAR =============\n========== 2 - SAIR ==============\n")

    escolha = int(input())
    if escolha == 1:
        jogo()
    else:
        print("Saindo...")
        exit()

menu()

