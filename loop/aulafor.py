'''for char in 'wrghehtrhrtdhrjt':
    print(char, end='')
    char = 1
    print(char)'''
'''for i in range(10, 1, -3):
    print(i)
    '''

'''senha_cad = '1234'
for i in range(3):
    senha = input("Senha: ")
    if senha == senha_cad:
        print("ACESSO LIBERADO")
        break
    print(f"hacker?????????vc tem só mais {2-i} tentativas!")
if senha != senha_cad:
    print("saí")
'''
#ex1 some todos o num de 1 a 10 usando for
'''cont = 0
for i in range(101):
    cont += i
print(cont)
'''
#ex2 peça 10 num para o usario e conte qts pares e impares
'''par = 0

impar = 0
for i in range(10):
    num = input("Digite um número")
    while not num.isnumeric():
        print("errado")
        num = input("Digite um número")
    num = int(num)
    if num % 2 == 0:
        par +=1
    else:
        impar+=1
print(f'par = {par}')
print(f'ímpar = {impar}')'''

#ex3 peça 10 num para o usario e faça soma e media
'''soma = 0
media = 0

for i in range(10):
    num = input("Digite um número")
    while not num.isnumeric():
        print("errado")
        num = input("Digite um número")
    num = int(num)
    soma +=num
media = soma/10
print(soma)
print(media)'''
#ex4 tabuada de 1 a 10
'''valor = 5
for i in range(11):
    tabuada = valor*i
    print(f'{valor}X{i} = {tabuada}')
'''
#ex5 qtd de vogais numa string digitada
'''vogais = 0
palavra = input("digite algo: ")
for i in palavra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vogais += 1
print(f'vogais {vogais} e {len(palavra)-vogais} consoantes')
'''

lista = [1, True, 3.2, 'danilo', ['asd',False]]
'''print(lista[1])
print(lista[4][0])
lista[4] = 'abc'
print(lista)
'''
'''lista[4] = 77
for i in range(5):
    print(lista[i])
'''
'''for elementos in lista:
    elementos = 1
    print(elementos)
print(lista)'''

'''for i in range(len(lista)):
    lista[i] = 1
print(lista)
'''

#ex6
'''profs = ['Andre', 'Lucas Silva', 'Yan', 'Allen',  'Fabio', 'Celso']
achou = False
for i in range(len(profs)):
    if profs[i] == 'Danilo':
        achou = True
        print(f'{profs[i]} está no índice {i}')
        break
if not achou:
    print("Não está aqui")'''
'''
profs = ['Andre', 'Lucas Silva', 'Yan', 'Allen',  'Fabio', 'Celso']
materia = ['Storytelling', 'Front-end', 'Edge', 'Software Experience', 'nada', 'Matemática']
achou = False
for i in range(len(profs)):
    print(f'{profs[i]} - {materia[i]}')
'''
#achar os profs em comum
profsA = ['Andre', 'Lucas Silva', 'Yan', 'Allen',  'Rita', 'Celso']
profsB = ['Romeu', 'Célia', 'Rita', 'Alexandre',  'Alex']
for profsA in profsB:
    for profsB in profsA:
        if profsA == profsB:
            print(f'{profsA} dá nas duas turmas, la ele')
