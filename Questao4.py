4. Um químico está fazendo uma análise de pH em alguns produtos para uma empresa
farmacêutica. O profissional terá que receber 12 valores do pH de determinados produtos e
analisar se são: ácidos, neutros ou básicos. Faça um algoritmo que ajude o químico nisso. A
função em Python deve receber a lista dos dados(pH) digitados dos produtos e separar cada
pH, em 3 listas, na seguinte situação:
 pH menor que 7: ácido
 pH igual a 7: neutro
 pH maior que 7 e até 14: básico

def classificar_ph(lista_ph):
    acidos = []
    neutros = []
    basicos = []

    for ph in lista_ph:
        if ph < 0 or ph > 14:
            print(f"Valor {ph} inválido!")
        elif ph < 7:
            acidos.append(ph)
        elif ph == 7:
            neutros.append(ph)
        else:
            basicos.append(ph)

    print(f"\nÁcidos (pH < 7): {acidos}")
    print(f"Neutros (pH = 7): {neutros}")
    print(f"Básicos (7 < pH ≤ 14): {basicos}")

lista_ph = []
print("=== Análise de pH ===")
for i in range(1, 13):
    ph = float(input(f"Digite o pH do produto {i}: "))
    lista_ph.append(ph)

classificar_ph(lista_ph)