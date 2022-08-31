# Multa por excesso de velocidade. 
v = int(input("Informe a velocidade que seu carro estava: "))
m =  (v - 80) * 7     
if v > 80: 
   print("Você recebera uma multa por excesso de velocidade no valor de :", m, "reais")
else:
    print("Você estava dentro dos limites de velocidade")