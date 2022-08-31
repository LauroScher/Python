# 1 Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C. 
a = float(input("Informe o 1° número: "))
b = float(input("Informe o 2° número: "))
c = float(input("Informe o 3° número: "))
if a + b < c: 
    print("A soma de {:.0f} com {:.0f} é menor que o número {:.0f}".format(a,b,c)) 
else: 
    print("Tente novamente")