#5.Faça um programa que solicite ao usuário 10 números inteiros. Em seguida
#informe o maior deles.
maior = 0
for num in range(1, 11):
    n = int(input(f'informe o {num}° número: '))
    if maior < n:
        maior = n 
print("O maior número é {}".format(maior))