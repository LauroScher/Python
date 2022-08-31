# 4.Faça um programa que solicite ao usuário 10 números inteiros. Em seguida
# informe o menor deles.

menor = 1000*1000
for num in range(1, 11):
    n = int(input(f'informe o {num}° número: '))
    if menor > n:
        menor = n 
print("O menor número é {}".format(menor))