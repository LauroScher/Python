# Número aleatorio 
from random import randint
c = randint(1, 5)
j = int(input("Fale um número de 1 a 5: "))
print("Parabéns você acertou" if j == c else "Desculpe, você erro!! Tente novamente")