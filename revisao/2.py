"""
um professor precisa sortear para diversos alunos. Esses alunos serão sorteados randomicamente,
o numero deve corresponder ao numero do diario.
"""
import random

#looping

while True:
    numero_aleatorio = random.randint(1,25)
    print(numero_aleatorio)
    resposta= input("Deseja sortear outro numero???? (S/N)").strip().lower()
    if resposta != "s":
        print ("encerando o sorteio")
        break



