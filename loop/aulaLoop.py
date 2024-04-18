'''par = 0
cont = 0
while True:
    num = int(input("Diga um numero: "))
    if num % 2 == 0:
        par = par + 1
    cont = cont + 1
    if cont >= 5:
        break

impar = 5-par
print(f'Foram {par} número(s) pares e {impar} números ímpares')
'''
'''cont = 1
senha = '1234'
password = input("Digite a sua senha: ")
while senha != password and cont<3:
    print(f"Ve é hacker? mais {3-cont} tentaivas")
    password = input("Digite a sua senha: ")
    cont = cont + 1

if senha == password:
     print("ACESSO PERMITIDO")
else:
    print("Sai hacker")
'''
#5050


'''soma = 0
i = 0
while i <= 100:
    soma += i
    i += 1
    print(soma)
print(soma)
'''
'''soma = 0
i = 0
while i <= 10:
    soma = soma + i**2
    i += 1
    print(soma)

print(soma)
'''

'''idoso = input("Você idoso? sim/não: ").upper()
while idoso != 'SIM' and idoso != 'NÃO':
    print("escreve direito")
    idoso = input("Você idoso? sim/não: ").upper()
if idoso == 'SIM':
    print("pdp")
else:
    print('paia')'''

while True:
    idoso = input("Você idoso? sim/não: ").upper()
    if idoso != 'SIM' or idoso != 'NÃO':
        break

'''valido = False
idoso = input("Você idoso? sim/não: ").upper()
while not (idoso == 'SIM' or idoso == 'NÃO'):
    print("escreve direito")
    idoso = input("Você idoso? sim/não: ").upper()
if idoso == 'SIM':
    print("pdp")
else:
    print('paia')
'''
'''
num = input("digite um número: ")
while not num.isnumeric():
    num = input("digite um número: ")
print(num)
print(type(num))'''
