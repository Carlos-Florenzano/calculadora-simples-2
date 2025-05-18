def obter_operacao():
    """Obtém a operação matemática desejada pelo usuário."""
    while True:
        operacao = input("Digite sum para soma, sub para subtração, div para divisão, e multi para multiplicação: ").lower()
        if operacao in ["sum", "sub", "div", "multi"]:
            return operacao
        else:
            print("Operação inválida. Por favor, digite sum, sub, div ou multi.")

def obter_quantidade_numeros():
    """Obtém a quantidade de números que o usuário deseja utilizar."""
    while True:
        try:
            quantidade = int(input("Quantos números você deseja utilizar para realizar a operação? "))
            if quantidade > 1:
                return quantidade
            else:
                print("Você precisa de pelo menos dois números para fazer o(s) cálculo(s)!!!")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

def obter_numeros(quantidade):
    """Obtém os números que o usuário deseja calcular."""
    numeros = []
    for i in range(quantidade):
        while True:
            try:
                numero = float(input(f"Digite o número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite um número válido.")
    return numeros

def calcular_soma(numeros):
    """Calcula a soma de uma lista de números."""
    return sum(numeros)

def calcular_subtracao(numeros):
    """Calcula a subtração de uma lista de números."""
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def calcular_multiplicacao(numeros):
    """Calcula a multiplicação de uma lista de números."""
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def calcular_divisao(numeros):
    """Calcula a divisão de uma lista de números."""
    resultado = numeros[0]
    if 0 in numeros[1:]:
        print("Erro: Não é possível dividir por zero.")
        return None
    else:
        for num in numeros[1:]:
            resultado /= num
        return resultado

def exibir_resultado(operacao, resultado):
    """Exibe o resultado da operação."""
    if resultado is not None:
        if operacao == "sum":
            print(f"Soma: {resultado}")
        elif operacao == "sub":
            print(f"Subtração: {resultado}")
        elif operacao == "multi":
            print(f"Multiplicação: {resultado}")
        elif operacao == "div":
            print(f"Divisão: {resultado}")

def calculadora():
    """Função principal que executa a calculadora."""
    print("Calculadora Simples das 4 Operações Matemáticas (2.0)!\n")
    operacao = obter_operacao()
    quantidade = obter_quantidade_numeros()
    numeros = obter_numeros(quantidade)

    if operacao == "sum":
        resultado = calcular_soma(numeros)
        exibir_resultado(operacao, resultado)
    elif operacao == "sub":
        resultado = calcular_subtracao(numeros)
        exibir_resultado(operacao, resultado)
    elif operacao == "multi":
        resultado = calcular_multiplicacao(numeros)
        exibir_resultado(operacao, resultado)
    elif operacao == "div":
        resultado = calcular_divisao(numeros)
        exibir_resultado(operacao, resultado)

if __name__ == "__main__":
    calculadora()