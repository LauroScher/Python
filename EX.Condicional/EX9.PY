#9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
#- para homens: (72.7 * h) – 58; 
#- para mulheres: (62.1 * h) – 44.7;
s = str(input("Informe se é homem ou mulher: ")).strip().lower()
h = float(input("Informe a sua altura em metros: "))
if s == "mulher": 
    p = (62.1 * h) - 44.7 
    print("Seu peso medio é {:.2f}kg".format(p))
else: 
    p = (72.7 * h) - 58
    print("Seu peso medio é {:.2f}kg".format(p))