# 2.Você como programador foi convidado a desenvolver um sistema da
# panificadora São José. Essa panificadora adota uma política de preços de
# desconto progressivo. o Cálculo do valor da unidade de pão é de R$0,18 de 1 a
# 10 pães, R$0,16 de 11 a 20 pães, R$0,13 de 21 a 30 pães, R$0,09 a partir de de
# 31 pães. Faça um algoritmo que receba a quantidade de pães desejada e calcule
# o preço total da compra.

un = int(input("Informe a quantidade de pão que deseja comprar: "))
valor = 0 
if un >= 1 and un <= 10:
    for quant in range(1, un + 1):
     valor = valor + 0.18
     print(f"{quant} unidades de é igual a {valor:.2f}")
elif un > 10 and un <= 20:
    for quant in range(1, un + 1):
     valor = valor + 0.16
     print(f"{quant} unidades de é igual a {valor:.2f}")
elif un > 20 and un <= 30:
    for quant in range(1, un + 1):
     valor = valor + 0.13
     print(f"{quant} unidades de é igual a {valor:.2f}")
elif un > 30:
    for quant in range(1, un + 1):
     valor = valor + 0.09
     print(f"{quant} unidades de é igual a {valor:.2f}")
print("O total a se pagar é R$ {:.2f}".format(valor))