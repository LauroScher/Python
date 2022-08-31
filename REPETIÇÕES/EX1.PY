# 1.Vamos ajudar uma criança a aprender a tabuada. Faça um programa que solicite
# um número de 1 a 9, e em seguida mostre a tabuada desse número. 

num = int(input("Informe um número interio de 1 a 9: "))
cont = 0
if num <= 9 and num >= 1: 
    for cont in range(0,11): 
     print(num,"x",cont,"=",num*cont)
else:
    print("O programa só aceita números de 1 a 9")