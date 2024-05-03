vinho1 = 'chapinha'
vinho2 = 'Sangue de boi'
vinho3 = 'Pérgola'
preco1 = 10
preco2 = 20
preco3 = 30
valor_total = 0
frete = 10
qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd = 0

opcoes = f'{vinho1} | {preco1} \n {vinho2} | {preco2} \n {vinho3} | {preco3}'
print("Seja bem-vindo(a) Vinheria Agnello!")
ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)
idade = 2024-ano
if idade < 18:
    print("nãoooooooooo podeeeeeeeeeeeeee")
else:
    while True:
        endereco = input("Diga seu endereço")
        print(f"essa sãqo nossas opções de vinhos: \n{opcoes}")
        escolha = input("qual lhe interessou? ")
        while not(escolha==vinho1 or escolha==vinho2 or escolha==vinho3):
            print(f"Opção inválida! somente essas {opcoes}")
            escolha = input("qual lhe interessou? ")
            qtd = input("quantos vinhos?" )
            while not qtd.isnumeric():
                qtd = input("quantos vinhos?" )
            qtd = int(qtd)
        if escolha == vinho1:
            valor_atual = preco1*qtd
            qtd1 += qtd
        elif escolha == vinho1:
            valor_atual = preco2*qtd
            qtd2 += qtd
        else:
            valor_atual = preco3*qtd
            qtd3 +=qtd
        valor_total += valor_atual
        proceder = input("Quer comprar mais?[s/n] ")
        while proceder != 's' or proceder != 'n':
            proceder = input("Quer comprar mais?[s/n] ")
        if proceder == 'n':
            break
    if valor_total > 500:
        frete = 0
        print("frete grátis")
    valor_total += frete
    print(f"você gastou R${valor_total} em \n"
        f"{qtd1} de {vinho1} \n {qtd2} de {vinho2} \n {qtd3} de {vinho3}"
        f"{endereco}")
