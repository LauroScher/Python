# 9.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
# crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça
# um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
# ou iguale a população do país B, mantidas as taxas de crescimento.Altere o programa permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

pa = int(input("Informe a quantidade populacional do país A: "))
ta = float(input("Informe sua taxa anual de crescimento do país A: "))
pb = int(input("Informe a quantidade populacional do país B: "))
tb = float(input("Informe sua taxa anual de crescimento do país B: "))
anos = 0
while pa == pb or ta == tb:
    print("Informe quantidades populacionais ou taxa populacionais diferentes") 
    pa = int(input("Informe a quantidade populacional do país A: "))
    ta = float(input("Informe sua taxa anual de crescimento do país A: "))
    pb = int(input("Informe a quantidade populacional do país B: "))
    tb = float(input("Informe sua taxa anual de crescimento do país B: "))
if pa != pb and ta != tb and pa < pb:
    while pa <= pb: 
     pa += pa*ta
     pb += pb*tb
     anos += 1
    print(f"Foram nessecários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B")
elif pa != pb and ta != tb and pa > pb:
    while pa >= pb: 
     pa += pa*ta
     pb += pb*tb
     anos += 1
    print(f"Foram nessecários {anos} anos para que a população do país B ultrapasse ou iguale a população do país A")