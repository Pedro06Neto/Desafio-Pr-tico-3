3. Você faz parte do grupo de analista de dados do Instituto Nacional de Meteorologia
(INMET). Todos os dias o setor captura os dados da temperatura. São 8 capturas no dia,
começando às 6h da manhã e terminando meia noite. Você deve criar um código para
armazenar os dados sobre a temperatura e tirar a média. Sobre a média da temperatura há
uma análise da seguinte forma:
 Temperatura menor que 20: baixa
 Temperatura entre 20 e 35: ideal
 Temperatura entre 36 e 50: em alerta
 Temperatura maior que 50: risco
A função do seu código deve ser para calcular e analisar a média.

def calcular_e_analisar_media(temperaturas):
    media = sum(temperaturas) / len(temperaturas)
    print(f"\nMédia da temperatura do dia: {media:.2f}°C")

    if media < 20:
        classificacao = "BAIXA"
    elif media <= 35:
        classificacao = "IDEAL"
    elif media <= 50:
        classificacao = "EM ALERTA"
    else:
        classificacao = "RISCO"

    print(f"Classificação: {classificacao}")

temperaturas = []

print("=== INMET - Registro de Temperaturas ===")
for i in range(1, 9):
    temp = float(input(f"Digite a {i}ª temperatura do dia: "))
    temperaturas.append(temp)

calcular_e_analisar_media(temperaturas)