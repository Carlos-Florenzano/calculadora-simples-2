print("Calculadora simples das 4 operações matemáticas:")

try:
    digitado = input("Digite sum para soma, sub para subtração, multi para multiplicação, ou div para divisão:")
    # o in é uma forma resumida desse if: if digitado == "sum" or digitado == "sub" or digitado == "multi" or digitado == "div":
    if digitado in ["sum", "sub", "multi", "div"]:
        if(digitado == "sum"):
            numero1 = float(input("Digite o numero 1:"))
            numero2 = float(input("Digite o numero 2:"))

            soma = numero1 + numero2
            print(soma)

        elif(digitado == "sub"): 
            numero1 = float(input("Digite o numero 1:"))
            numero2 = float(input("Digite o numero 2:"))

            subtracao = numero1 - numero2
            print(subtracao)

        elif(digitado == "multi"):
            numero1 = float(input("Digite o numero 1:"))
            numero2 = float(input("Digite o numero 2:"))

            multiplicacao = numero1 * numero2
            print(multiplicacao)

        elif(digitado == "div"):
            numero1 = float(input("Digite o numero 1:"))
            numero2 = float(input("Digite o numero 2:"))

            divisao = numero1 / numero2
            print(divisao)
except ValueError:
    print("Entrada inválida! Certifique-se de digitar apenas números válidos para os cálculos.")