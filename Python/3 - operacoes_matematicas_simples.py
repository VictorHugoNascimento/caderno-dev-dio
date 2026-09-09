numero1 = int(input("Digite o primeito número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
numero2 = int(input("Digite o segundo número: "))

if operacao == "+":
    print(f"A soma dos números é {numero1 + numero2}")
elif operacao == "-":
    subtracao = abs(numero1 - numero2)
    print(f"A subtração dos números é {subtracao}")
elif operacao == "*":
    print(f"A multiplicação dos números é {numero1 * numero2}")
elif operacao == "/":
    if numero2 == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"A divisão dos números é {numero1 / numero2}")
else:
    print("Operação inválida. Por favor, escolha entre +, -, *, /.")