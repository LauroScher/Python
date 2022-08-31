# 3.Vamos fazer um jogo. Defina um número secreto. Em seguida, solicite um
# número ao usuário. Caso o usuário acerte, exiba a mensagem “Parabéns! Você
# acertou.” Caso o valor digitado seja menor que o número secreto, exiba “Ainda
# não. Escolha um número maior”. Caso o valor digitado seja maior, exiba a
# mensagem “Ainda não. Escolha um número menor.” . O jogo só termina quando
# o usuário acertar o número secreto.

random = 23
num = int(input("Advinhe qual é o número secreto: "))
while num != random:
    if num < random: 
        num = int(input("Ainda não! Escolha um número maior e informe novamente: "))
    else:
        num = int(input("Ainda não! Escolha um número menor e informe novamente: "))
if num == random: 
    print("Parábens!! Você acertou o número secreto {}".format(random))