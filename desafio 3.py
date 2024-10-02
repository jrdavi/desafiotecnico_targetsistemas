'''
3) Observe o trecho de código abaixo: 
int INDICE = 12, 
SOMA = 0, 
K = 1; 
enquanto K < INDICE faça 
{ K = K + 1; SOMA = SOMA + K; } imprimir(SOMA); 
'''

#calculo da soma de 2+3+[n]... até 12
#o total deve ser 77

indice = 12
soma = 0
q = 1

while q<indice:
    q = q+1
    soma = soma + q

print(soma)
