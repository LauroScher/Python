# 8.Faça um programa que leia e valide as seguintes informações:
# a.Nome: maior que 3 caracteres;
# b.Idade: entre 0 e 150;
# c.Salário: maior que zero;
# d.Sexo: 'f' ou 'm';
# e.Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Informe seu Nome: ")).strip()
while len(nome) < 3: 
    print("Nome inválido")
    nome = str(input("Informe seu Nome: ")).strip()
idade = int(input("Informe sua idade: "))
while idade < 0 or idade > 150: 
    print("Idade inválida")
    idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salário: "))
while not salario > 0: 
    print("Salário inválido")
    salario = float(input("Informe seu salário: "))
sexo = str(input("Informe seu sexo (*F* para feminino e *M* para masculino): ")).strip().upper()
while sexo != 'M' and sexo != 'F':
    print("Sexo inválido")
    sexo = str(input("Informe seu sexo (*F* para feminino e *M* para masculino): ")).strip().upper()
print("Informe *s* para solteiro , *c* para casado, *v* para viúvo(a) e *d* para divorciado")
estadoC = str(input("Estado civil atual: ")).strip().lower()
while estadoC != "s" and estadoC != "c" and estadoC != "v" and estadoC != "d": 
    print("Informação inválida")
    print("Informe *s* para solteiro , *c* para casado, *v* para viúvo(a) e *d* para divorciado")
    estadoC = str(input("Estado civil atual: ")).strip().lower()