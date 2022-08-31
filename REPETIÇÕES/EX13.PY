# 13. Faça um programa que solicite dois números ao usuário entre 0 e 20. Em
#seguida imprima na tela todos os números que existem no intervalo.

print("----"*25)
print("Informe dois números diferentes, entre 0 e 20, e mostraremos todos os valores entre eles")
print("----"*25)
num1 = int(input("Informe um número inteiro de 0 a 20: "))
num2= int(input("Informe outro número inteiro de 0 a 20: "))
cont = 0
if num1 > 20 or num2 > 20:
    print("O programa não aceita valores maiores que 20")
elif num1 > num2:
    print("Os números dentro dos intervalos entre {} e {} são:".format(num2,num1), end=(" "))
    for cont in range(num2, num1 - 1):
        num2 += 1  
        print(num2, end=(" "))
elif num1 < num2:
    print("Os números dentro dos intervalos entre {} e {} são:".format(num1,num2), end=(" "))
    for cont in range(num1, num2 - 1):
        num1 += 1 
        print(num1, end=(" "))