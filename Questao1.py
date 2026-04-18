#1. Crie um sistema de calculadora com funções. Cada operação matemática deve ser tratada em uma função.
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = int(input("Escolha a operação: "))
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == 1:
        print(f"Resultado: {somar(a, b)}")
    elif opcao == 2:
        print(f"Resultado: {subtrair(a, b)}")
    elif opcao == 3:
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcao == 4:
        print(f"Resultado: {dividir(a, b)}")
    else:
        print("Opção inválida!")

calculadora()