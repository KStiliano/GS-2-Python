from helpers import forca_opcao

def exibir_diagrama():
    print("\nDiagrama de informações:\n"
          "Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n "
          "- entre 30 e 50% = estado ideal\n - entre 51 e 69% = em alerta de chuva\n"
          "\nTemperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - "
          "abaixo de 25ºC = temperatura baixa\n - entre 51 e 79 = temperatura em alerta\n"
          "\nProximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
          "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n")

def print_de_opcoes_circuitos(circuitos):
    print("\nCircuitos disponíveis:")
    for id_circuito, dados in circuitos.items():
        print(f"{id_circuito} - {dados['nome']}")

def exibir_resultado(circuito_id):
    dados = circuitos[circuito_id]
    print(f"\nResultado: O circuito de {dados['nome']} está com umidade de {dados['umidade']}%, "
          f"temperatura de {dados['temperatura']}ºC, e proximidade de {dados['proximidade']} metros.")

def print_de_opcoes_pilotos(pilotos):
    print("\nPilotos disponíveis:")
    for piloto_id, dados in pilotos.items():
        print(f"{piloto_id} - {dados['nome']}")

def exibir_dados_piloto(piloto_id):
    dados = pilotos[piloto_id]
    print(f"\nDados do piloto {dados['nome']}:\n"
          f"Equipe: {dados['equipe']}\n"
          f"Nacionalidade: {dados['nacionalidade']}\nColocação: {dados['colocacao']}\nPontos: {dados['pontos']}")

def sys_dados():
    opcoes = ['0', '1', '2', '3']
    print(f"Bem-vindo ao banco de dados Mahindra Racing!")
    while True:
        tipo_dado = forca_opcao("Deseja acessar dados do circuito ou dos pilotos? (1 - Circuito, 2 - Pilotos)\n--> ",
                                opcoes, "Opção inválida!")
        if tipo_dado == '1':
            print_de_opcoes_circuitos(circuitos)
            circuito_id = forca_opcao("Digite o ID do circuito:\n--> ", circuitos.keys(), "Circuito inválido!")
            tipo_exibicao = forca_opcao("Você deseja ver opções detalhadas (1) ou específicas (2)?\n--> ", opcoes,
                                        "Opção inválida!")
            if tipo_exibicao == '1':
                exibir_diagrama()
                exibir_resultado(circuito_id)
            else:
                dado = forca_opcao("Qual dado específico deseja ver?\n1 - Umidade\n2 - Temperatura\n3 - Proximidade\n--> ",
                                   opcoes, "Opção inválida!")
                if dado == '1':
                    print(f"Umidade: {circuitos[circuito_id]['umidade']}%")
                elif dado == '2':
                    print(f"Temperatura: {circuitos[circuito_id]['temperatura']}ºC")
                elif dado == '3':
                    print(f"Proximidade: {circuitos[circuito_id]['proximidade']} metros")
        elif tipo_dado == '2':
            print_de_opcoes_pilotos(pilotos)
            piloto_id = forca_opcao("Digite o ID do piloto:\n--> ", pilotos.keys(), "ID do piloto inválido!")
            exibir_dados_piloto(piloto_id)
        continuar = forca_opcao("Deseja fazer uma nova pesquisa? (1 - Sim, 0 - Não)\n--> ", opcoes, "Opção inválida!")
        if continuar == '0':
            break

circuitos = {
    "1": {"nome": "Mônaco", "umidade": 35, "temperatura": 30, "proximidade": 50},
    "2": {"nome": "São Paulo", "umidade": 60, "temperatura": 11, "proximidade": 150},
    "3": {"nome": "Paris", "umidade": 25, "temperatura": -5, "proximidade": 200},
    "4": {"nome": "Miami", "umidade": 60, "temperatura": 30, "proximidade": 499},
    "5": {"nome": "Tokyo", "umidade": 30, "temperatura": 5, "proximidade": 379},
    "6": {"nome": "Rome", "umidade": 10, "temperatura": 35, "proximidade": 250},
    "7": {"nome": "México", "umidade": 50, "temperatura": 31, "proximidade": 175},
    "8": {"nome": "Buenos Aires", "umidade": 50, "temperatura": 10, "proximidade": 100},
    "9": {"nome": "Punta del Este", "umidade": 20, "temperatura": 20, "proximidade": 200}
}

pilotos = {
    "1": {"nome": "Jordan King", "equipe": "Mahindra", "nacionalidade": "Grã-Bretanha", "colocacao": 26, "pontos": 0},
    "2": {"nome": "Edoardo Mortara", "equipe": "Mahindra", "nacionalidade": "Suíça", "colocacao": 16, "pontos": 20},
    "3": {"nome": "Nyck De Vries", "equipe": "Mahindra", "nacionalidade": "Holanda", "colocacao": 18, "pontos": 18},
    "4": {"nome": "Pascal Wehrlein", "equipe": "Porsche TagHeur", "nacionalidade": "Alemanha", "colocacao": 1, "pontos": 198},
    "5": {"nome": "Mitch Evans", "equipe": "Jaguar TOS", "nacionalidade": "Nova Zelândia", "colocacao": 2, "pontos": 192},
    "6": {"nome": "Nick Cassidy", "equipe": "Jaguar TOS", "nacionalidade": "Nova Zelândia", "colocacao": 3, "pontos": 176},
    "7": {"nome": "Lucas Di Grassi", "equipe": "ABT Cupra", "nacionalidade": "Brasil", "colocacao": 23, "pontos": 4},
    "8": {"nome": "Jake Hughes", "equipe": "Neom McLaren", "nacionalidade": "Grã-Bretanha", "colocacao": 14, "pontos": 48}
}
