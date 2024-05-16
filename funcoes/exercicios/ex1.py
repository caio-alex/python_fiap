#Ex1
'''def lista():
    numeros = []
    while True:
        entrada = input("Digite um número ou x para sair: ")
        if entrada == 'x':
            break
        else:
            numero = int(entrada)
            numeros.append(numero)
    return numeros

numeros = lista()
print("Tu inseriu os números ", numeros)'''

#Ex2
'''def lista():
    numeros = []
    while True:
        entrada = input("Digite um número ou x para sair: ")
        if entrada == 'x':
            break
        else:
            numero = int(entrada)
            numeros.append(numero)
    return numeros

numeros = lista()
print("Tu inseriu os números ", numeros)
maior = max(numeros)
print("o maior é", maior)'''

#Ex3
'''def inserir_palavras():
    palavras = []
    while True:
        entrada = input("Digite uma palavra ou x pra sair ")
        if entrada == 'x':
            break
        palavras.append(entrada)
    return palavras

def filtrar_palavras_a(lista_palavras):
    palavras_com_a = [palavra for palavra in lista_palavras if palavra.lower().startswith("a")]
    return palavras_com_a

print("Digite uma palavra ou x pra sair ")
palavras_usuario = inserir_palavras()

palavras_com_a = filtrar_palavras_a(palavras_usuario)

print("Palavras que começam com a letra a:", palavras_com_a)'''

'''def inserir_numeros():
    numeros = []
    while True:
        entrada = input("Número: ")
        if entrada == 'x': 
            break
        if entrada.isnumeric(): 
            numeros.append(int(entrada))
            print(numeros)
        else:
            print("Entrada inválida. Digite um número válido ou 'x' para sair.")
    return numeros

def numeros_pares(lista_numeros):
    pares = [par for par in lista_numeros if par % 2 == 0]
    return pares

print("Digite um número ou x para sair")
numeros_usuario = inserir_numeros()

pares = numeros_pares(numeros_usuario)

print("Números pares:", pares)
'''

#Ex5
