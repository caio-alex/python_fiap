total = 0
italia = 3
espanha = 4
chileno = 5
precoItalia = 40
precoEspanha = 60
precoChileno= 70
frete = 20
print("Seja bem-vindo(a) a vinheria Agnello!")
while True:
    ano_nasc = input("Diga o seu ano de nascimento: ")
    if ano_nasc.isnumeric():
        ano_nasc = int(ano_nasc)
        break
    print("Você não digitou o ano corretamente!")

idade = 2024-ano_nasc

if idade < 18:
    print("menores de 18 anos não podem comprar bebidas alcoolicas, seu boboca!")
else:
    endereco = input("diga seu endereço: ")
    while True:
        print()
        print("compras acima de R$100 é frete grátis")
        print(f"Opções de vinhos\n [1]Vinho Itália R$40 Em estoque: {italia}\n [2]Vinho Espanha R$60 Em estoque: {espanha}\n [3]Vinho Chileno R$70 Em estoque: {chileno}\n")
        
        vinho = input("Insira o número do vinho: ")
        if vinho.isnumeric():
            vinho = int(vinho)
            
        quantidade = input("Quantos vinhos quer?: ")
        if quantidade.isnumeric():
            quantidade = int(quantidade)
        
        if vinho == 1:
            valor = precoItalia*quantidade
            italia -= quantidade
            if italia < 0:
                print("esgotado")    
                if quantidade > italia:
                    italia = italia+quantidade
                else:
                    italia = 0
                continue

        elif vinho == 2:
            valor = precoEspanha*quantidade
            espanha -= quantidade
            if espanha < 0:
                print("esgotado")
                if quantidade > espanha:
                    espanha = espanha+quantidade
                else:
                    espanha = 0
                continue

        elif vinho == 3:
            valor = precoChileno*quantidade
            chileno -= quantidade
            if chileno < 0:
                print("esgotado")
                if quantidade > chileno:
                    chileno = chileno+quantidade
                else:
                    chileno = 0
                continue
                            
        print(f'valor da escolha R${valor}')
        total += valor
        print(f'preço total no carrinho R${total}')
        retornar = input("Deseja compra mais vinhos? [sim][nao]: ")
        if retornar == 'sim':
            continue

        elif retornar == 'nao':
            if total > 100:
                print()
                print("Frete grátis")
                print(f"O valor total da compra foi de R${total} no endereço {endereco}")

            else:
                print("Frete de R$20")
                totalFrete = total+frete
                print(f"O valor total da compra com frete foi de R${totalFrete} no endereço {endereco}")
            print("Obrigado pela compra!")
            break