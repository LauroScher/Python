# 11.A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
# série até o n−ésimo termo.

quant = int(input("Informe qual termo deseja ver na seguência de Fibonacci: "))
t1 = 0
t2 = 1
aux = 3 
while aux <= quant:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    aux += 1
print(t3)