#Ex1 
'''nota = int(input("Digite a nota de 0 a 10: "))
while nota < 0 or nota > 10:
    nota = input("Digite a nota de 0 a 10: ")

print(f'a nota é {notaInt}')
print(type(notaInt))'''

'''nota = input("Digite a nota de 0 a 10:\n ")
while not nota.isnumeric():
    nota = input("Digite a nota de 0 a 10: ")

n = int(nota)

while n<0  or n > 10:
    n = input("Digite a nota de 0 a 10: ")
print(f'a nota é {n}')'''

#corrigido
'''while True:
    num = input('Digite a nota de 0 a 10: ')
    if num.isnumeric():
        num = int(num)
        if num > 0 and num < 10:
            print(num)
            break
        else:
            print('não digitou um número entre 0 e 10')
    else:
        print("não é um número")'''
#Ex2
'''nome = input("Nome: ")
while len(nome) <= 3:
    nome = input("Nome: ")

idade = input("idade: ")
while not idade.isnumeric():
    idade = input("idade: ")
idade = int(idade)
while idade < 0 or idade>150:
    idade = int(input("idade: "))


salario = input("Salário: ")
while not salario.isnumeric():
    salario = input("Salário: ")
salario = int(salario)
while salario < 0:
    salario = input("Salário: ")

sexo = input("Sexo(f/m): ")
while sexo!='f' or sexo !='m':
    sexo = input("Sexo: f/m").upper()

EstadoCivil = input("s, c, v, d: ")
while EstadoCivil !='s' or EstadoCivil !='c' or EstadoCivil !='v' or EstadoCivil !='d':
    EstadoCivil = input("s, c, v, d: ")

print(f'nome: {nome}, idade: {idade}, salario: {salario}, sexo: {sexo}, Estado Civil: {EstadoCivil}')
'''
'''while True:
    nome = input("Nome: ")
    if len(nome)>3:
        break
print(nome)

while True:
    idade = int(input("Idade: "))
    if idade < 150 and idade >=0:
        break
print(idade)


while True:
    salario = int(input("Salário: "))
    if salario > 0:
        break
print(salario)

while True:
    sexo = input("Sexo: ")
    if sexo == 'm' or sexo =='f':
        break
print(sexo)

while True:
    EstadoCivil = input("s, c, v, d: ")
    if EstadoCivil =='s' or EstadoCivil =='c' or EstadoCivil =='v' or EstadoCivil =='d':
        break
print(EstadoCivil)

print(f'nome: {nome}')
print(f'idade: {idade}')
print(f'salario: {salario}')
print(f'sexo: {sexo}')
print(f'Estado Civil: {EstadoCivil}')'''

#Ex3
'''paisA = 80000
paisB = 200000
ano = 0
while paisA < paisB:
    paisA *= 1.03
    paisB *= 1.015
    ano += 1
print(f'{ano} anos')'''

#Ex4 
'''cont = 0
soma = 0
while cont < 5:
    nota = input(f"diga o {cont+1}° número\n")
    while not nota.isnumeric():
        nota = input(f"diga o {cont+1}° número\n")
    nota = int(nota)
    cont += 1
    soma += nota
        
print(f'soma: {soma}')
print(f'media: {soma/5}')'''

#novo
'''cont = 0
soma = 0
while cont < 5:
    nota = input(f"diga o {cont+1} número\n")
    while not nota.isnumeric():
        nota = input(f"diga o {cont+1} número\n")
    nota = int(nota)
    cont += 1
    soma += nota

print(f'soma: {soma}')
print(f'media: {soma/5}')
'''
#Ex5 ++
'''A = int(input("Primeiro: "))
B = int(input("Ultimo: "))
i = A
while i<B-1:
    i += 1
    print(i)'''
#Corrigido

'''A = input("número: ")
while not A.isnumeric():
    A = input("número: ")

B = input("número: ")
while not B.isnumeric():
    B = input("número: ")

if B < A:
    aux = A
    A = B
    B = aux

while A <= B:
    print(A)
    A += 1'''
#Ex6
'''while True:
    nome = input("nome: ")
    
    senha = input("senha: ")
    if nome != senha:
        break
    else:
        print("não pode senha igual ao nome de usuário!")
print(senha)
print(nome)'''

#corrigido
'''nome = input("nome: ")
senha = input("senha: ")
while nome == senha:
    print("não pode senha igual ao nome de usuário!")
    nome = input("nome: ")
    senha = input("senha: ")
print(senha)
print(nome)'''
#Ex7
'''numero = input("Tabuada do ")
while not numero.isnumeric():
    numero = input("Tabuada do ")
numero = int(numero)
i = 0
while i < 10:
    i += 1

    print(f'{numero}X{i} = {numero*i}')
'''
#Novo
'''numero = 1
i = 1
while numero <= 10:
    print(f'Tabuada do {numero}')
    i = 1
    while i <= 10:
        print(f'{numero}X{i}= {numero*i}')
        i += 1
    numero += 1'''

#Ex8 +++
'''n = int(input('Quantos termos quer? '))
a = 1 #1° termo
b = 1 #2° termo
print(a, end=' ')
print(b, end=' ')

i = 2#contador dos termos
while i < n: #enquanto o contador for menor que a sequência pedida:
    c = a + b
    print(c, end=' ') #as variaveis
    a = b 
    b = c 

    i += 1'''

#Ex9
'''par = 0
i = 0
while True:
    numero = input("Número: ")
    while not numero.isnumeric():
        numero = input("Número: ")
    numero = int(numero)
    i += 1
    if numero % 2 == 0:
        par += 1
    if i >= 10:
        break
impar = 10-par
print(f'par {par}')
print(f'ímpar {impar}')
'''
par = 0
impar = 0
i = 0
while i < 10:
    numero = input(f"Número {i+1}: ")
    if not numero.isnumeric():
        continue # volta para o while
    numero = int(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    i += 1

print(f'par {par}')
print(f'ímpar {impar}')



#Ex10 +
'''
num = int(input("Número fatorial: "))
fat = 1
i = 0
while i < num:
    i += 1
    fat *= i
    print(i, fat)'''
#corrigido
'''num = input("Diga um número")
while not num.isnumeric():
    num = input("Diga um número")
num = int(num)
fatorial = num
fatorial_s = f'{num}! = {num}'
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_s += f'*{num}'
fatorial_s += f' = {fatorial}'
print(fatorial_s)
'''
'''num = input("Número fatorial: ")
while not num.isnumeric():
    num = input("Número fatorial: ")
fat = 1
while num > 0:
    fat = fat * num #fat = 1*5 -> fat = 5 -> fat = 5*4 -> fat = 20 -> fat = 20*3 -> fat = 60...
    num -= 1
print(fat)'''


#Ex11
'''while True:
    numero = input("Diga um número: ")
    while not numero.isnumeric():
        numero = input("Diga um número: ")
    numero = int(numero)
    if numero % 2 != 0 and numero % 3 != 0  and numero % 5 != 0:
        print("É primo")
        break
    else:
        print("não é primo")
'''
#corrigido
'''
i = 2
numero = input("Diga um número: ")
numero = int(numero)
while i < numero/2:
    print(f"{numero}%{i} = {numero%i}")
    if numero % i == 0:
        print("não é primo")
        break
    i += 1
if i >= numero/2:
    print("primo")'''

#Ex12
'''i = 0
soma = 0
notas = input("Quantas notas deseja?")
while not notas.isnumeric():
    notas = input("Quantas notas deseja?")
notas = int(notas)
while True:
    nota = input("Nota: ")
    i += 1
    soma += nota
    if i >= notas:
        break
media = soma / notas
print(f'média: {media}')
'''

#Ex13
'''salario = input("Digite se salário: ")
while not salario.isnumeric():
    salario = input("Digite se salário: ")
salario = int(salario)
aumento = 1.5/100
ano = 1996
while ano < 2024:
    ano += 1
    aumento *= 2
    salario *= 1 + aumento

    print(ano, f'- {aumento:.2f}% - R${salario:.2f}')
    '''
#Ex14
'''i = 0
a = 0
b = 0
c = 0
d = 0
while True:
    numero = input("Número: ")
    while not numero.isnumeric():
        numero = input("Número: ")
    numero = int(numero)
    i += 1
    if numero < 0:
        break
    if numero <= 25:
        a += 1
        print(f"o número {numero} foi o {a} número de 0-25")
    elif numero <= 50:
        b += 1
        print(f"o número {numero} foi o {b} número de 26-50")
    elif numero <=75:
        c += 1
        print(f"o número {numero} foi o {c} número de 51-75")
    elif numero <= 100:
        d += 1
        print(f"o número {numero} foi o {d} número de 76-100")'''

#Ex15
'''i = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

while True:
    print("*|*|"*10, "Urna Eleitoral", "*|*|"*10)
    print("Candidatos", "-"*85)
    print("[1]Ronaldinho Gaúcho | [2]Wagner Sanches | [3]Arboleda | [4]Rey Mysterio | [5]VOTO NULO | [6]VOTO EM BRANCO")
    voto = int(input("Voto: "))
    i += 1
    if voto == 0:
        print(f'Foram {i-1} votos. ')
        porcentagem_nulo = (e / (i-1)) * 100
        print(f'Porcentagem de votos nulos: {porcentagem_nulo:.2f}%')
        porcentagem_branco = (f / (i-1)) * 100
        print(f'Porcentagem de votos em branco {porcentagem_branco:.2f}%')
        print(f'{a} para Ronaldinho Gaúcho, {b} para Wagner Sanches, {c} para Arboleda, {d} para Rey Mysterio, {e} para VOTO NULO e {f} para VOTO EM BRANCO')
        break

    if voto == 1:
        a += 1
        print("Você votou em Ronaldinho Gaúcho")
    if voto == 2:
        b += 1
        print("Você votou em Wagner Sanches")
    if voto == 3:
        c += 1
        print("Você votou em Arboleda")
    if voto == 4:
        d += 1
        print("Você votou em Rey Mysterio")
    if voto == 5:
        e += 1
        print("Você votou em Nulo")
    if voto == 6:
        f += 1
        print("Você votou em Branco")'''
