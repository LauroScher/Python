# 10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles e mostre sua soma.

num1 = int(input("Informe o 1° número inteiro: "))
num2 = int(input("Informe o 2° número inteiro: ")) 
print("Os números compreendidos nos intervalos são: ", end=(""))
soma = 0
if num1 < num2: 
    for num1 in range(num1, (num2 - 1)): 
     num1 += 1
     print(num1, end=(" "))
     soma += num1
    print("e sua soma é",soma)
else: 
    for num2 in range(num2, (num1 - 1)): 
     num2 += 1
     print(num2, end=(" "))
     soma += num2
    print("e sua soma é",soma)