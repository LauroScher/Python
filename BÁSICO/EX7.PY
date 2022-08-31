#Soma dos impares multiplos de 3 (1 a 500)
s = 0
print("Os números impares multiplos de 3 são: ")
for i in range(1, 501, 2): 
    if i % 3 == 0:
     s += i
     print(i, end=" ")     
print('')
print("Sua soma é", s)