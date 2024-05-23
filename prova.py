def calcula_idade():
    while True:
        ano = input("Digite seu ano de nascimento: ")
        if ano.isnumeric():
            idade = 2024 - int(ano)
            return idade
        
def chama_endereco():
    endereco = input("Diga o seu endereço: ")
    return endereco

def escolher_vinho():
    vinhos = {'Argentino': 80, 'Espanhol': 120, 'Italiano': 200}
    for vinho, preco in vinhos.items():
        print(f"{vinho} - R${preco}")
    escolha = input("Escolha um vinho: ")
    while escolha not in vinhos:
        escolha = input("Vinho não encontrado. Escolha um vinho: ")
    print(f"Você escolheu {escolha}. Preço: R${vinhos[escolha]}")
    
    return escolha, vinhos[escolha]

def escolher_qtd():
    while True:
        qtd = input("Quantas garrafas? ")
        if qtd.isnumeric():
            return int(qtd)
        
def escolher_continuar():
        proceder = input('Deseja continuar?[s][n]')
        return proceder
            
def calculo_frete(total_geral):
    frete = 30
    if total_geral > 500:
        return total_geral
    else:
        return total_geral+frete
    
idade = calcula_idade()
if idade < 18:
    print("sai daqui")
else:
    endereco = chama_endereco()
    total_geral = 0
    carrinho = {}
    while True:
        vinho, preco = escolher_vinho()
        qtd = escolher_qtd()
        total = qtd * preco
        total_geral += total 

        if vinho in carrinho:
            carrinho[vinho]+=qtd
        else:
            carrinho[vinho] = qtd

        print(f"Você escolheu {qtd} garrafa(s) de {vinho}, com valor de : R${total:.2f}")
        print(f'Total no carrinho: R${total_geral}')
        continuar = escolher_continuar()
        if continuar == 's':
            continue
        else:
            total_geral_frete = calculo_frete(total_geral)
            if total_geral > 500:
                print("Frete Grátis")
            else:
                print("Frete de R$30")
            for vinho, qtd in carrinho.items():
                print(f'vinho {vinho}: {qtd} garrafas')
            print(f'Total será de R${total_geral_frete}')
            print(f"Seu pedido será enviado para: {endereco}")
            print("Obrigado pela compra")
            break
