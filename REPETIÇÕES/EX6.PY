# 6.Um atleta olímpico de salto participou das olimpíadas do brasil e fez um total de
# 5 saltos. Faça um programa que solicite a distância atingida pelo atleta em cada
# salto e exiba: O tamanho médio dos saltos, o menor salto e o maior salto.

maior = 0 
menor = 100
media = 0
for num in range(1, 6):
    n = float(input(f'informe a distância do {num}° salto em metros: '))
    media += n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
print("A média dos saltos foi {:.2f} ".format(media/5)) 
print("O maior salto foi {} e o menor foi {}".format(maior,menor))