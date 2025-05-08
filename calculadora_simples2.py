qtd = 0

try:
    print("Calculadora Simples das 4 Operações Matemáticas (2.0)!\n")
    digitado = input("Digite sum para soma, sub para subtração, div para divisão, e multi para multiplicação:")
    if digitado in ["sum","sub", "div", "multi"]:
        qtd = int(input("Quantos números você deseja utilizar para realizar a operação?"))
    if qtd <=1:
        print("Você precisa de pelo menos dois números para fazer o(s) cálculo(s)!!!")
    else:
        numeros = []

        for i in range(qtd):
            numero = float(input(f"Digite o número {i + 1}: "))
            numeros.append(numero)

        if(digitado == "sum"):
            resultado = sum(numeros)
            print(f"Soma: {resultado}")
        elif(digitado == "sub"):
            resultado = numeros[0]
            for num in numeros[1:]: # o "1:" em numeros[1:] manda pegar todos os elementos a partir do índice 1 (ou seja, ao invés de começar com um índice 0, ele começa com um índice 1 (é como o i = 1 do for da linguagem C, porém ele cria uma nova lista que começa nesse índice 1))
                resultado -= num 
                # resultado -= num é o mesmo que: resultado = resultado - num, só que -= tem um melhor desempenho pelo interpretador Python (que costuma otimizar internamente o operador composto -=)
                print(f"Subtração: {resultado}")
        elif(digitado == "multi"):
            resultado = 1 # nesse caso o resultado = 1 pois é o elemento neutro da multiplicação
            for num in numeros:
                resultado *= num
                print(f"Multiplicação: {resultado}")
        elif(digitado == "div"):
            resultado = numeros[0]
            if 0 in numeros[1:]:
                print("Erro: Não é possível dividir por zero.")
            else:
                for num in numeros[1:]:
                    resultado /= num
                    print(f"Divisão: {resultado}")

except ValueError:
    print("Entrada inválida! Certifique-se de digitar apenas números válidos para os cálculos.")
    