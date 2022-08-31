#MAIOR E MENOR 

maior = 0 
menor = 1000*1000
for num in range(1, 5):
    n = int(input(f'informe o {num}° número: '))
    if maior < n:
        maior = n
    if menor > n:
        menor = n 
print("O maior número da operação é {} e o menor é {}".format(maior,menor))