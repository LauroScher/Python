#FATORIAL
num = int(input("Informe o número inteiro para saber seu fatorial: "))
cont = num
fat = 1
print(num,"! =", end=" ")
while cont > 0: 
    print(cont, end=" ")
    print('x' if cont > 1 else '=', end=" ")
    fat *= cont
    cont -= 1
print(fat, end=" ")