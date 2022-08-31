# 2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “mulher” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 
n = str(input("Informe o seu nome: "))
s = str(input("Homem ou mulher: ")).strip().lower()
e = str(input("Solteiro(a) ou casado(a): ")).strip().lower()
if s == 'mulher' and e == 'casada': 
    t = str(input("Informe quantos anos tem seu casamente: "))
    print("Humm!!",t,"anos de casada")
    print("Oi, casada")
else:
    print("fim do programa")