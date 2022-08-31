#Jogo da advinhação 

from random import randint
random = randint(1, 10)
num = int(input("Advinhe qual é o meu número de 1 a 10: "))
tentativas = 1
while num != random: 
    num = int(input("Você erro!! informe novamente: "))
    tentativas += 1
if num == random: 
    print("Parábens!! Você acertou na sua",tentativas,"° tentativa.")