import random
from helpers import meu_index, limpar_tela
from game_dictionaries import dict_game_forca
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

games = {
    "1": {"name": "Eco Forca", "game": game_forca}
}