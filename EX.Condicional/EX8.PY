#8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.
x = float(input("Informe o 1° número: "))
y = float(input("Informe o 2° número: "))
z = float(input("Informe o 3° número: "))
if x > y and x > z and y > z:
    print("A ordem decrescente é {:.0f}, {:.0f}, {:.0f}".format(x,y,z))
elif y > x and y > z and x > z:
    print("A ordem decrescente é {:.0f}, {:.0f}, {:.0f}".format(y,x,z))
elif z > x and z > y and y > x:
    print("A ordem decrescente é {:.0f}, {:.0f}, {:.0f}".format(z,y,x))
elif x > y and x > z and y < z:
    print("A ordem decrescente é {:.0f}, {:.0f}, {:.0f}".format(x,z,y))
elif y > x and y > z and x < z:
    print("A ordem decrescente é {:.0f}, {:.0f}, {:.0f}".format(y,z,x))
elif z > x and z > y and y < x:
    print("A ordem decrescente é {:.0f}, {:.0f}, {:.0f}".format(z,x,y))
else: 
    print("Coloque valores diferentes")