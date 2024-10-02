'''
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e 
o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um 
programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência. 
'''

numero_inserido = int(input())

n = 0
numero_a = 0
numero_b = 1

if n>=0:
    while n<numero_inserido:
        n = numero_a + numero_b
        numero_a = numero_b
        numero_b = n
if n==numero_inserido:
    print("O número pertece ao Fibonacci")
else:
    print("O número não pertece a sequencia Fibonacci")

