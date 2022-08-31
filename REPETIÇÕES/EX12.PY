#12 Faça um programa que leia um nome de usuário e a sua senha e não aceite a
#senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
#pedir as informações. As informações devem ser solicitadas enquanto o usuário
#digitar as informações incorretas.

nome = str(input("Informe o nome do usuário: ")).strip().lower()
senha = str(input("Informe sua senha usando caracteres: ")).strip().lower()
while nome == senha:
    print("-----"*20) 
    print("Não aceitamos senha igual o nome do usuário")
    print("-----"*20) 
    print("Faça um nova senha")
    print("-----"*20) 
    nome = str(input("Informe o nome do usuário: ")).strip().lower()
    senha = str(input("Informe sua senha usando caracteres: ")).strip().lower()
print("-----"*20) 
print("Cadastro feito com sucesso")
print("-----"*20)