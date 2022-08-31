#Qual é seu sexo ?
s = str(input("Informe seu sexo( F = feminino e M = mascúlino): ")).strip().upper()
while s != 'F' and s != 'M': 
    s = str(input(" Inválido!! Escreva somente F = feminino e M = mascúlino): ")).strip().upper()
if s == "F": 
    print("Seja bem vinda, madame") 
elif s == "M": 
    print("Seja bem vindo, rapaz")