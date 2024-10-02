'''
4) Descubra a lógica e complete o próximo elemento: 
a) 1, 3, 5, 7, ___ 
b) 2, 4, 8, 16, 32, 64, ____ 
c) 0, 1, 4, 9, 16, 25, 36, ____ 
d) 4, 16, 36, 64, ____ 
e) 1, 1, 2, 3, 5, 8, ____ 
f) 2,10, 12, 16, 17, 18, 19, ____ '''


#a) resposta: 9
numero_A = 1
for n in range(4):
    numero_A = numero_A + 2
print ("A)", numero_A)

#b) resposta: 128
numero_B = 2
for n in range(6):
    numero_B = numero_B * 2
print("B)", numero_B)
    
#c) resposta: 49
numero_C = 0
for n in range(8):
    numero_C = n**2
print("C:", numero_C)
    
#d) resposta: 100
numero_D = 4
for n in range(5):
    numero_D = (2 * (n+1)) ** 2
print("D:", numero_D)

#e) resposta: 13
numero_E = [0,1]
for n in range(6):
    numero_E[0], numero_E[1] = numero_E[1], numero_E[0] + numero_E[1]

print("E:)", numero_E[1])

#f) resposta: 200
#numeros iniciados por extenso iniciados com a letra D

print("D:) 200")
