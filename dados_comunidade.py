import json
import matplotlib.pyplot as plt

def carregar_dados(arquivo_json='dados.json'):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    return dados

def exibir_dados_estado(dados, estado):
    if estado in dados:
        print(f"\nDados para o estado de/do/da {estado}:")
        nomes_metrica = {
            "consumo_energia": "Consumo de energia (kW/h)",
            "co2_emissoes": "Emissões de CO2 (Mt)",
            "consumo_ideal": "Consumo ideal (kW/h)",
            "economia_financeira": "Economia financeira (Em milhares de R$)"
        }
        for key, value in dados[estado].items():
            nome_formatado = nomes_metrica.get(key, key.capitalize())
            if key == 'economia_financeira':
                print(f"{nome_formatado}: R${value}")
            else:
                print(f"{nome_formatado}: {value}")
        economia_potencial = dados[estado]['economia_financeira']
        print("\nSugestões para economizar:")
        print(f"Se os usuários no estado de {estado} reduzissem o uso de ar-condicionado em horários de pico, luzes em cômodos vazios e equipamentos em modo stand-by, poderiam economizar aproximadamente R${economia_potencial} ao mês.")
    else:
        print("Estado não encontrado.")

def gerar_grafico_estado(dados, estado):
    if estado in dados:
        labels = ["Consumo de Energia (kW/h)", "Emissões de CO2 (Mt)", "Consumo Ideal (kW/h)", "Economia Financeira (Em milhares de R$)"]
        valores = [dados[estado]["consumo_energia"],
                   dados[estado]["co2_emissoes"],
                   dados[estado]["consumo_ideal"],
                   dados[estado]["economia_financeira"]]
        cores = ['yellow', 'red', 'blue', 'green']
        plt.figure(figsize=(10, 5))
        plt.bar(labels, valores, color=cores)
        plt.title(f'Dados de Consumo - Estado {estado}')
        plt.xlabel('Métricas')
        plt.ylabel('Valores')
        plt.grid(True)
        plt.show()
    else:
        print("Estado não encontrado.")

def gerar_comparacao(dados, estado1, estado2):
    if estado1 in dados and estado2 in dados:
        labels = ["Consumo de Energia (kW/h)", "Emissões de CO2 (Mt)", "Consumo Ideal (kW/h)", "Economia Financeira (Em milhares de R$)"]
        valores_estado1 = [dados[estado1]["consumo_energia"],
                           dados[estado1]["co2_emissoes"],
                           dados[estado1]["consumo_ideal"],
                           dados[estado1]["economia_financeira"]]
        valores_estado2 = [dados[estado2]["consumo_energia"],
                           dados[estado2]["co2_emissoes"],
                           dados[estado2]["consumo_ideal"],
                           dados[estado2]["economia_financeira"]]
        cores_estado1 = ['green', 'green', 'green', 'green']
        cores_estado2 = ['yellow', 'yellow', 'yellow', 'yellow']
        x = range(len(labels))
        largura_barra = 0.3
        plt.figure(figsize=(12, 6))
        plt.bar([p - largura_barra/2 for p in x], valores_estado1, width=largura_barra, label=f"{estado1}", color=cores_estado1)
        plt.bar([p + largura_barra/2 for p in x], valores_estado2, width=largura_barra, label=f"{estado2}", color=cores_estado2)
        plt.title(f'Comparação de Dados - {estado1} vs {estado2}')
        plt.xlabel('Métricas')
        plt.ylabel('Valores')
        plt.xticks(x, labels)
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Um ou ambos os estados não foram encontrados.")

def consultar_dados():
    dados = carregar_dados()
    while True:
        print("Estados disponíveis:", ", ".join(dados.keys()))
        estado = input("Digite a sigla do estado que deseja consultar (ex: SP, RJ, etc.) ou digite 'sair' para voltar ao menu principal: ").upper()
        if estado == "SAIR":
            break
        if estado in dados:
            exibir_dados_estado(dados, estado)
            gerar_grafico = input("Deseja ver um gráfico dos dados? (s/n): ").lower()
            if gerar_grafico == 's':
                gerar_grafico_estado(dados, estado)
                comparar = input("Deseja comparar com outro estado? (s/n): ").lower()
                if comparar == 's':
                    estado2 = input("Digite a sigla do segundo estado: ").upper()
                    gerar_comparacao(dados, estado, estado2)
        else:
            print("Estado não encontrado no banco de dados.") 
        pesquisar_novamente = input("Deseja fazer outra pesquisa? (s/n): ").lower()
        if pesquisar_novamente == 'n':
            print("Obrigado por usar o sistema! Até logo.")
            break
        elif pesquisar_novamente != 's':
            print("Entrada inválida! Tente novamente.")
