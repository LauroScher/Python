#Menu básico 

print("Seja bem vindo ao meu programa")
print("Após solicitar os valores números de X e Y, escolha uma das opções de nosso menu")
print("****MENU****")
print("Para [1] - Soma // Para [2] - multiplicar // Para [3] - qual valor é maior // Para [4] - novos valores // Para [5] - sair do programa")
x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))
menu = int(input("Qual das opcões do menu você deseja executar: "))
while not menu == 5: 
    if menu == 1:    
        print("{:.0f} + {:.0f} = {:.0f}".format(x,y,(x+y)))
        menu = int(input("Solicite uma nova operação ou informe [5] para sair: "))
    elif menu == 2: 
        print("{:.0f} x {:.0f} = {:.0f}".format(x,y,(x*y)))
        menu = int(input("Solicite uma nova operação ou informe [5] para sair: "))
    elif menu == 3: 
        if x > y: 
            print("O número {:.0f} é maior".format(x))
        else: 
            print("O número {:.0f} é maior".format(y))
        menu = int(input("Solicite uma nova operação ou informe [5] para sair: "))
    elif menu == 4:
        x = float(input("Informe um novo valor para x: "))
        y = float(input("Informe um novo valor para y: "))
        menu = int(input("Solicite uma nova operação ou informe [5] para sair: "))
    elif menu > 5: 
        print("Número inválido!!")
        menu = int(input("Solicite números dentro do menu informado ou informe [5] para sair: "))
if menu == 5: 
    print("Fim do programa!!")