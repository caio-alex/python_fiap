'''vinhos = ['Argentino', 'Bucarest', 'Chileno']
for vinho in vinhos:
    print(vinho)


vinhos = ['Argentino', 'Bucarest', 'Chileno']
i = 0
for vinho in range(len(vinhos)):
    print(vinho)
    i +=1
print(i)'''
'''senha_cad = '1234'
for i in range(3):
    senha = input("Digite sua senha: ")
    if senha == senha_cad:
        print("acesso liberado")
        break
    print(f"você só tem {2-i} tentativas")
print("sai daqui")'''

'''cont = 0
for i in range(11):
    print(i)
    cont += i
print(cont)
'''
'''par = 0
impar = 0
for i in range(10):
    numero = input("digite um número: ")
    numero = int(numero)
    print(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
print(par)
print(impar)'''
'''soma = 0
media = 0

for i in range(10):
    numero = input("Digite um número: ")
    numero = int(numero)
    soma += numero
    print(soma)
media = soma/10
print(f"soma é {soma}")
print(f'média é {media}')'''

'''profs = ['Andre', 'Lucas Silva', 'Danilo', 'Yan', 'Allen',  'Fabio', 'Celso']
achou = False
for i in range(len(profs)):
    if profs[i] == 'Danilo':
        achou = True
        print(f'{profs[i]} está no índice {i}')
        break
if not achou:
    print("Não está aqui")
'''
'''vinhos = ['ARGENTINO', 'ITALIANO', 'ESPANHOL']
achou = False
while not achou:
    vinho_procurado = input('Escolha um vinho: ').upper()
    for vinho in vinhos:
        if vinho == vinho_procurado:
            achou = True
            break
if achou:
    print(f'você escolheu o vinho {vinho}')
'''
achou = False
vinhos = ['Argentino', 'Italiano', 'Espanhol']
precos = ['80,00', '120,00', '200,00']
for i in range(len(vinhos)):
    msg = print(f'vinho {vinhos[i]} custa {precos[i]}')
while not achou:
    vinho_procurado = input(f"qual vinho?\n ")
    for vinho in vinhos:
        if vinho == vinho_procurado:
            achou = True
            break
if achou:
    print(f'o vinho escolhido foi {vinho}')