#Preço da passagem 
p = int(input("Informe a distância da sua viagem em Km: "))
if p > 200: 
    print("O valor da sua passagem será:", p*0.45, "reais")
else: 
    print("O valor da sua passagem será:", p*0.5, "reais")