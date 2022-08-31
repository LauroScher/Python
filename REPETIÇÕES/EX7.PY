#7.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.

nota = float(input("Informe a sua nota: "))
while nota > 10 or nota < 0: 
    nota = float(input("Valor inválido! Informe um valor de 0 a 10: "))
print("fim do programa!!")