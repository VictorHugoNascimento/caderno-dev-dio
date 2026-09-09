palavra = input("Digite uma palavra: ")

palavra_invertida = palavra[::-1].strip().lower()

if palavra_invertida == palavra[::-1].strip().lower():
    print(f"A palavra '{palavra}' É um palíndromo.")
else:
    print(f"A palavra '{palavra}' NÃO é um palíndromo.")