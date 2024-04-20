'''Nome: Caio Alexandre dos Santos RM:558460'''

print("***Bem-vindo(a) a vinheria Agnelo!***")

ano = int(input("Seu ano de nascimento: "))
idade = 2024-ano
if idade < 18:
    print("Não é permitido a venda de bebidas alcoolicas para menores de 18 anos!")
else:
    endereco = input("Digite seu endereço: ")
    print("***Opções de Vinhos***")
    print("Taxa do frete com compras abaixo de R$100 será de R$30")
    vinho = int(input("[1]Vinho Branco R$ 30,00 | [2] Vinho tinto R$40,00 | [3]Vinho rosé R$ 50,00: "))
    garrafas = int(input("Quantas garrafas? "))
    if vinho == 1:
        valor = 30*garrafas

    elif vinho == 2:
        valor = 40*garrafas

    elif vinho == 3:
        valor = 50*garrafas

    if valor <= 100:
        valorFrete = valor+30
        print((f"Valor final terá frete de R$30,00 e será de R${valorFrete} no endereço {endereco}"))
        print("Obrigado pela compra")
    else:
        print("Frete grátis")
        print(f"Valor final de R${valor} no endereço {endereco}")
        print("Obrigado pela compra")