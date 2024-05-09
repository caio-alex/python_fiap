'''def expo(x, y):
    return (x ** y)
print(expo(2, 5))
print(expo(3, 2))
print(expo(5, 3))

'''
'''def voto(x, y):
    if y < 16:
        return (x, False)
    else:
        return(x, True)

#===================================

while True:
    eleitor = input("nome do candidato: ")
    idade = int(input("idade: "))
    while not idade.isnumeric():
        idade = input("idade: ")
    idade=int(idade)

    if not idade: break

    teste1, teste2 = voto(eleitor, idade)

    if teste2:
        print('pode votar')
    else:
        print('nao pode votar')

print('fim')'''


'''def maior(x):
    z = x[0]
    for i in x:
        if z < i:
            z = i
    return(z)

y = [-2, -5, -7, -9]
print(maior(y))

t = [2, 5, 7, 9]
print(maior(t))'''

'''def maior(x, y):
    if x > y:
        print(f'if {x}')
    else:
        print(f'else {y}')

maior(2, 5)
maior(8, 5)
maior(2, 1)

maior("2", "a")
maior("*", "/")'''

def cpf(x):
    digito
     pos = 11
     for i in x:
        if pos > 3:
            digito1 += int(i) * (pos-1)
            digito2 += int(i) * pos
            pos -= 1

    digito2 = digito1 * 2
    digito2 = digito2 % 11
    digito2 = 11 - digito2
    if digito2 > 9:
        digito2 = 0
    return(digito1, digito2)
