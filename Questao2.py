2. Faça um programa que receba uma quantidade determinada de números (o usuário que
irá determinar quantos números irá digitar). Armazene todos os números digitados em uma
lista. O programa deverá:
 mostrar quantos números pares e ímpares existem na lista;
 mostrar todos os números pares e ímpares digitados.
Crie uma função para fazer essa ação.

def analisar_numeros(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]

    print(f"\nQuantidade de números pares: {len(pares)}")
    print(f"Números pares: {pares}")
    print(f"\nQuantidade de números ímpares: {len(impares)}")
    print(f"Números ímpares: {impares}")

quantidade = int(input("Quantos números você vai digitar? "))
numeros = []

for i in range(quantidade):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

analisar_numeros(numeros)