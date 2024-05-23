'''#imposto de renda
precos = [80, 120, 200]

precosB = [1000, 3000]

def calculaImposto(preco):
    impostoIR = 0.2*preco
    impostoISS = 0.3*preco
    impostoTotal = impostoIR + impostoISS

    return impostoTotal

for preco in precos:
    imposto_total = calculaImposto(preco)
    print(imposto_total)

for preco in precosB:
    imposto_total = calculaImposto(preco)
    print(imposto_total)
'''
#pedir idade 
#endereço
#força opção
#escolher o vinho:preço
#qtd de garrafas
#comprar mais vinhos
#mostrar as ofertas com join e erro em ordem crescente de valor
#frete
#mostrar qtd de vinho cada um
#total final
def calcula_idade(idade):
    idade = 2024 - ano
    return idade >=18

def escolher_vinho(vinhos):
    print('escolha um vinho')
    print(' - '.join(vinhos),vinhos)

vinhos = ['Argentino', 'Espanhol', 'Italiano']
precos = [80, 120, 200]


ano = input("digite seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("digite sua idade: ")
ano = int(ano)
if calcula_idade(ano):
    endereco = input("digite seu endereço: ")
    print(f"Endereço fornecido: {endereco}")
else:
    print("sai daqui")

