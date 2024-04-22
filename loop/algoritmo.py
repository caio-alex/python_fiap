import math
i = 2
numero = input("Diga um número: ")
numero = int(numero)
raiz = math.sqrt(numero)
while i < raiz:
    i+=1
    if numero % i == 0:
        print("não é primo")
        break
    else:
        print("Primo")
        break
    






















'''while i < numero/2:
    print(f"{numero}%{i} = {numero%i}")
    if numero % i == 0:
        print("não é primo")
        break
    i += 1
if i >= numero/2:
    print("primo")'''