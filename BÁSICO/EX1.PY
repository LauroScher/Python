#ANALISE DA LETRA A
frase = str(input("Escreva uma frase e analisaremos as letras A: ")).strip()
print('A frase possui {} letras A'.format(frase.lower().count('a')))
print('A letra A apareceu pela primeira vez na posição {}'.format(frase.lower().find("a")+1))
print('A letra A apareceu pela última vez na posição {}'.format(frase.lower().rfind("a")+1))