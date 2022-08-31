# 4) Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.   
x = int(input("Informe o valor inteiro de x: "))
y = int(input("Informe o valor inteiro de y: "))
if x == y: 
    print("Os números sãos iguais e sua soma é", x + y)
else: 
    print("Os números são diferente e sua multiplicação é", x*y)