'''
Escreva um programa que verifique, em uma string, 
a existência da letra ‘a’, seja maiúscula ou minúscula, 
além de informar a quantidade de vezes em que ela ocorre. 
'''

entrada_string = str(input())

contagem = 0
a = ["a", "A", "à", "á", "À", "Á","ã", "Ã"]

for n in entrada_string:
    if n in a:
        contagem+=1

if contagem>0:
    print(f"Contém {contagem} 'a's na string")
else:
    if contagem<=0:
        print( "Não contém 'a's na string")
