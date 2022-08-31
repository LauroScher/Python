#- O sistema deve conter um loop que solicite a ação do usuário sobre os seguintes aspectos: 
# 0 - Para sair do sistema, 1- Entrar no sistema - 2 - para cadastrar um usuário( Id, Nome e Idade ), 
# 3 - Mostrar na tela o usuário cadastrado

usuario = str(input("Informe seu nome de usuário: ")).strip()
menu = int(input(f"Seja bem vindo {usuario}! Para entrar em nosso programa digite [1]: "))
while menu != 0: 
    if menu == 1: 
        print("Você entrou em nosso sistema")        
        menu = int(input("Digite [2] para fazer o cadastro de seus dados: "))
    elif menu == 2: 
        id = int(input("Crie um ID usando digitos númericos: "))
        idade = int(input("Informe sua idade: "))
        print(f"Ao usuário ({id}) {usuario} de {idade} anos de idade, parabéns! Seus dados foram cadastrados com sucesso")
        menu = int(input("Digite [3] para mostrar : "))
    elif menu == 3:
        print(f"{usuario} esta adorar cursar a cadeira de programção, pois assim aprendeu colocar sua criatividade em pratica e realizar seu sonho de ser um programador. ")
        print("Existiu dificuldade no começo, mas o esforço própio foi compensador")
        menu = int(input("Digite [0] para sair do programa: "))  
    else: 
        print("Número inválido")
        menu = int(input(f"Seja bem vindo {usuario}! Para entrar em nosso programa digite [1]: "))
if menu == 0: 
    print("Você saiu do programa")
    print("Obrigado por usar nosso sistema")