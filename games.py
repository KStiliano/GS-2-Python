import random
from helpers import meu_index, limpar_tela
from game_dictionaries import dict_game_forca, perguntas_quiz, desafios_consumo
from cadastro_login import usuarios

def game_forca():
    word = random.choice(dict_game_forca['words'])
    index = meu_index(dict_game_forca['words'], word)
    guessed = ["_"] * len(word)
    tries = 10
    print("\nBem vindo a Eco Forca!\nComo jogar: digite letras individualmente até alguma dela aparecer no display,\nfaça isso até formar a palavra completa.\nAtenção!\nHá palavras com mais de uma palavra, essas não possuirão espaço entre elas\nAs palavras não possuem assento ou 'ç'\n")
    while tries > 0:
        print(" ".join(guessed))
        print(f"Dica: {dict_game_forca['tips'][index]}")
        guess = input(f"Você tem {tries} tentativas\nDigite uma letra:\n--> ").upper()
        limpar_tela()
        if guess in word:
            print("Bom trabalho!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Oops, tente de novo!")
            tries -= 1
        if "_" not in guessed:
            print("Você conseguiu! A palavra era", word)
            return True
    print("Fim de jogo! A palavra era", word)
    return False

def quiz_sustentavel(perguntas):
    print("Bem-vindo ao Quiz Sustentável!")
    pontuacao = 0
    perguntas_aleatorias = random.sample(list(perguntas.items()), len(perguntas))
    for pergunta, (opcoes, resposta_correta) in perguntas_aleatorias:
        print("\n" + pergunta)
        for i, opcao in enumerate(opcoes):
            print(opcao)
        resposta = input("Escolha sua resposta (A-E): ").strip().upper()
        if resposta in "ABCDE" and ord(resposta) - ord("A") == resposta_correta:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Errado! A resposta correta era: {opcoes[resposta_correta][3:]}")
    print(f"\nQuiz terminado! Sua pontuação final foi: {pontuacao}/{len(perguntas)}")
    if pontuacao == len(perguntas):
        print("Parabéns! Você acertou todas as perguntas sobre sustentabilidade!")
    elif pontuacao >= 6:
        print("Ótimo trabalho! Continue aprendendo sobre práticas sustentáveis.")
    else:
        print("Não fique triste com o resultado, vamos continuar aprendendo! Práticas sustentáveis são o caminho para o futuro.")

def desafio_consumo_sustentavel(desafios):
    print("Bem-vindo ao Desafio de Consumo Sustentável!")
    consumo_total = 0
    co2_total = 0
    desafios_aleatorios = random.sample(desafios, len(desafios))
    for desafio in desafios_aleatorios:
        print("\n" + desafio["descricao"])
        for i, (opcao, consumo, co2) in enumerate(desafio["opcoes"], start=1):
            print(f"{i}) {opcao} - Consumo: {consumo} kWh, Emissão de CO₂: {co2} kg")
        escolha = int(input("Escolha uma opção (1-3): ")) - 1
        if 0 <= escolha < len(desafio["opcoes"]):
            consumo_escolhido, co2_escolhido = desafio["opcoes"][escolha][1], desafio["opcoes"][escolha][2]
            consumo_total += consumo_escolhido
            co2_total += co2_escolhido
            print(f"\nVocê escolheu: {desafio['opcoes'][escolha][0]}")
            print(f"Impacto desta escolha: {consumo_escolhido} kWh e {co2_escolhido} kg de CO₂.")
        else:
            print("Escolha inválida, opção ignorada.")
    print(f"\nDesafio concluído! Seu consumo total foi de {consumo_total:.2f} kWh e sua emissão de CO₂ foi de {co2_total:.2f} kg.")
    if consumo_total < 2:
        print("Parabéns! Você é um exemplo de sustentabilidade!")
    elif consumo_total < 4:
        print("Ótimo trabalho! Suas escolhas são bastante sustentáveis.")
    elif consumo_total < 6:
        print("Bom esforço! Mas há espaço para melhorar nas escolhas diárias.")
    else:
        print("Vamos continuar aprendendo sobre sustentabilidade para fazer escolhas mais conscientes no futuro.")

def games_menu(usuario):
    while True:
        print("Escolha um jogo:")
        for key, game in games.items():
            print(f"{key}. {game['name']}")
        choice = input("Digite o número da escolha: ")
        if choice in games:
            if games[choice]["game"]():
                play_again = input("Deseja jogar novamente? (s/n): ")
                if play_again.lower() == "s":
                    limpar_tela()
                    continue
                else:
                    if usuario['primeira_vez']:
                        usuario['primeira_vez'] = False
                        usuario['ECs'] += 1500
                        print(f"{usuario['username']}, por ter jogado pela primeira vez algum de nossos jogos, você receberá 1000 ECs de bônus")
                    break
            else:
                play_again = input("Deseja jogar novamente? (s/n): ")
                if play_again.lower() == "s":
                    limpar_tela()
                    continue
                else:
                    if usuario['primeira_vez']:
                        usuario['primeira_vez'] = False
                        usuario['ECs'] += 1500
                        print(f"{usuario['username']}, por ter jogado pela primeira vez algum de nossos jogos, você receberá 1000 ECs de bônus")
                    break
        else:
            print("Opção inválida. Tente novamente!")
    return

games = {
    "1": {"name": "Eco Forca", "game": game_forca},
    "2": {"name": "Eco Quiz", "game": quiz_sustentavel},
    "3": {"name": "Desafio de Consumo", "game": desafio_consumo_sustentavel}
}