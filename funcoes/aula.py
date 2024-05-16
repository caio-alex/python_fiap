'''def checa_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num
ano = checa_numero("diga seu ano de nascimento: ")
print(ano)
qtd = checa_numero("diga a qtd de garrafas: ")
print(qtd)

def soma_numeros(a,b):
    return a+b
num1 = 1
num2 = 2
soma = soma_numeros(num1, num2)
print(soma)
'''


'''def meu_in(lista_elementos, elemento):

    for i in range(len(lista_elementos)):
        if lista_elementos[i] == elemento:
            return True
    return False
lista = [55, 77, 333, 6, 3, 5643, 5, 11, 43, 555,224]
buscar = 333
ta_ou_num_ta = meu_in(lista, buscar)
print(ta_ou_num_ta)
professores = ['Danilo', 'lucas', 'Andre', "Fabio", 'Celso', 'Yan', 'Allen']
prof = 'Danilo'
prof_ta_ou_jum_ta = meu_in(professores, prof)
print(prof_ta_ou_jum_ta)'''
#ex1 função que recebe uma lista de numeros e retorna a soma deles

'''def soma_ele(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma
lista=[1,2,3,4,5]
res = soma_ele(lista)
print(res)

'''

#ex2 função que recebe uma lista de numeros e retorna uma lista de pares
'''def lista_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares
lista=[1,2,3,4,5]
par = lista_pares(lista)
print(par)'''

#ex3 função que recebe uma string e conta a qtd de vogais
'''
def conta_vogais(palavra):
    vogais = 0
    for char in palavra:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vogais += 1
    return vogais
palavra = 'algumacoisa'
vogal = conta_vogais(palavra)
print(vogal)
'''

#ex4 função de escolher o vinho

'''def escolher_vinho(msg, lista_opcoes, erro):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        escolha = input(msg)
    return escolha
vinhos = ['vinho1', 'vinho2', 'vinho3']
opcoes = ['continuar', 'não']
opcao = escolher_vinho("diga seu vinho: ", vinhos)
continuar = escolher_vinho("continuar ou não\n", opcoes)'''

def encontra_maior(numeros):
    indice_maior = 0
    maior = numeros[indice_maior]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
            indice_maior = i
    return indice_maior

def busca_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] ==  elemento:
            return i

precos = [10, 20, 100000, 50, 5]
carros = ['up', 'uno', 'celta', 'gol', 'kombi']
local_carro = encontra_maior(precos)
print(f"o carro {carros[local_carro]} "
      f"custa{precos[local_carro]}")
