# GS-2-Python

## Integrantes 👋
<ul> 
    <li>João Marcelo Furtado Romero (RM555199)</li>
    <li>Kayky Silva Stiliano (RM555148)</li>
</ul>

## Instruções
O arquivo ```app.py``` é o arquivo principal que deve ser rodado e é recomendado usar o terminal no tamanho 75% ou tela cheia.

## Explicação do Projeto 📖
Um app gamificado em Python da EcoSphere, que dá ao usuário escolhas de seção onde há uma seção de games, uma seção de dados capturados pelos dispositivos G.A.C.O onde o usuário escolhe qual dado ele deseja ver tendo a possibilidade de fazer novas pesquisas também. Por fim há uma seção de loja onde o usuário pode comprar merchandise entre outros produtos da EcoSphere com as EcoCoins, moedas virtuais que são de uso exclusivo do site.

## Dependências 📦
<ul>
    <li>matplotlib</li>
    <li>json</li>
    <li>random</li>
</ul>
<br>

## Explicando o <a href="path">Código</a> 🧑‍💻
 
```c
def limpar_tela(linhas=10):
    print("\n" * linhas)
```
Essa função imprime várias linhas em branco para "limpar" a tela do console, o padrão é 10.
<br>
<hr>

```c
def forca_opcao(msg, opcoes, msg_erro):
    opcao = input(msg)
    while opcao not in opcoes:
        limpar_tela()
        print(msg_erro)
        opcao = input(msg)
    return opcao
```
Exibe uma mensagem (`msg`) e espera a entrada do usuário.
<br>
Continua solicitando uma opção válida (que esteja dentro do parâmetro `opcoes`) até o usuário digitar corretamente.
<br>
Se a entrada for inválida, imprime uma mensagem de erro (`msg_erro`) e limpa a tela antes de pedir novamente.
<hr>

```c
def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False
```
Essa função `meu_index` procura por um elemento em uma lista e retorna a posição (índice) dele, caso o encontre. Se o elemento não estiver na lista, a função retorna `False`.
<hr>

```c
def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)
```
Essa função força o usuário a inserir um número válido.
Parâmetros: `msg`: Mensagem a ser exibida ao solicitar a entrada do usuário.
<br>
`msg_erro`: Mensagem de erro a ser exibida se a entrada não for um número.
<br>
Descrição: Solicita a entrada do usuário. Se a entrada não for numérica, exibe uma mensagem de erro e repete a solicitação até que um número seja inserido.
<br>
Retorno: O número inserido pelo usuário, convertido para inteiro.
<hr>

```c
def print_de_opcoes(lista, line_break=True):
    output = '\n'.join([f'- {item}' for item in lista]) if line_break else ', '.join(lista)
    print(output)
    return output1
```
Imprime uma lista de itens, um por linha se `line_break` for `True` (padrão), ou em uma única linha separada por vírgulas se for `False`.
<br>
Retorna a string formatada para possível reutilização.
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻

```c
def cadastrar_usuario():
    def solicitar_input(mensagem):
        while True:
            entrada = input(mensagem).strip()
            if entrada:
                return entrada
            else:
                print("Este campo não pode ficar vazio.")
    username = solicitar_input("Digite o nome de usuário para cadastro:\n--> ")
    if username in usuarios:
        print("Usuário já existe!")
        return None  
    senha = solicitar_input("Digite sua senha:\n--> ")
    email = solicitar_input("Digite seu email:\n--> ")
    is_admin = solicitar_input("O usuário é admin? (s/n):\n--> ").lower() == 's'
    if is_admin:
        ecs_inicial = 200000  
    else:
        ecs_inicial = 2500

    usuarios[username] = {
        "senha": senha, 
        "email": email, 
        "admin": is_admin, 
        "primeira_vez": True,
        "saldo_compras": [], 
        "ECs": ecs_inicial, 
        "carrinho": {},
        "endereco": {
            "estado": '',
            "rua": '',
            "numero": '',
            "complemento": '',
            "cep": ''
        }
    }
    print("Cadastro realizado com sucesso!")
    return login()
```
Solicita dados como nome de usuário, senha e email para cadastrar um novo usuário (Caso for vazio, a função auxiliar retorna a opção novamente.) e verifica se o nome de usuário já existe no dicionário `usuarios`. 
<br>
Define um saldo inicial de EcoCoins (ECs) de 200.000 para administradores e 2.500 para usuários normais.
<br>
Adiciona o novo usuário ao dicionário `usuarios` com suas respectivas informações. Após o cadastro, tenta realizar o login chamando a função `login()`.
<hr>

```c
def login():
    username = input("Digite o nome de usuário:\n--> ")
    if username not in usuarios:
        print("Usuário não encontrado!")
        return None  
    senha = input("Digite sua senha:\n--> ")
    if usuarios[username]["senha"] == senha:
        print(f"\nBem-vindo, {username}!")
        return {"username" : username, **usuarios[username]}  
    else:
        print("Senha incorreta!")
        return None
```
Solicita o nome de usuário e a senha para login. Verifica se o nome de usuário existe no dicionário `usuarios` e se a senha está correta. Se a autenticação for bem-sucedida, retorna as informações do usuário. Se falhar, exibe mensagens de erro apropriadas.
<hr>

```c
usuarios = {
    "admin": {
        "senha": "admin123", 
        "email": "admin@email.com", 
        "admin": True, 
        "primeira_vez": True,
        "saldo_compras": [], 
        "ECs": 200000, 
        "carrinho": {},
        "endereco": {
            "estado": 'estado',
            "rua": 'rua',
            "numero": 'numero',
            "complemento": 'complemento',
            "cep": 'cep'
        }
    },
    "user": {
        "senha": "userpass", 
        "email": "user@email.com", 
        "admin": False, 
        "primeira_vez": True,
        "saldo_compras": [], 
        "ECs": 2500, 
        "carrinho": {},
        "endereco": {
            "estado": 'estado',
            "rua": 'rua',
            "numero": 'numero',
            "complemento": 'complemento',
            "cep": 'cep'
        }
    }
}
```

Um dicionário que armazena informações dos usuários, onde as chaves são os nomes de usuário, e os valores são outros dicionários contendo senha, email, permissões de administrador, primeira vez jogando os minigames, saldo de compras, Mahindra Coins, carrinho de compras e o endereço.
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻

```c
from helpers import forca_opcao, limpar_tela
from sys_functions import sys_dados
from cadastro_login import cadastrar_usuario, login
from shop import loja, produtos_disponiveis, produtos
from games import games_menu
```
Descrição: Importa as funções `forca_opcao` e `limpar_tela` do módulo `helpers`, a função `consultar_dados` do módulo `dados_comunidades`, a função `cadastrar_usuario` e `login` do módulo `cadastro_login`, a função `loja`, a função `produtos_disponiveis` e o dicionário `produtos` do módulo `shop` e a função `games_menu` do módulo `games`.
<hr>

```c
from helpers import forca_opcao, limpar_tela
from dados_comunidade import consultar_dados
from cadastro_login import cadastrar_usuario, login
from shop import loja, produtos_disponiveis, produtos
from games import games_menu

opcoes = ['0', '1', '2', '3', '4']
nome_da_empresa = "EcoSphere"
usuario = None  
while True:
    print()
    if usuario:
        print(f"Seja bem-vindo(a), {usuario['username']} à {nome_da_empresa}!")
    else:
        print(f"Seja bem-vindo à {nome_da_empresa}!!!")
    caminho = forca_opcao("Por qual caminho você deseja seguir:\n"
                          "1 - Jogos\n"
                          "2 - Dados\n"
                          "3 - Loja\n"
                          "4 - Cadastro/Login\n"
                          "0 - Sair\n--> ", opcoes, "Opção inválida!")
    limpar_tela()
    if caminho == '1':
        if usuario:
            games_menu(usuario)
        else:
            print('\nVocê precisa estar logado para jogar.')
    elif caminho == '2':
        consultar_dados()
    elif caminho == '3':
        if usuario:
            loja(usuario)
        else:
            produtos_disponiveis()
            print("\nVocê precisa estar logado para acessar as funcionalidades da loja.")
    elif caminho == '4':
        opcao_login = forca_opcao("1 - Cadastro\n2 - Login\n--> ", opcoes, "Opção inválida!")
        if opcao_login == '1':
            usuario_atual = cadastrar_usuario()
            if usuario_atual:
                usuario = usuario_atual
        elif opcao_login == '2':
            usuario_atual = login()
            if usuario_atual: 
                usuario = usuario_atual
    elif caminho == '0':
        break

```
O arquivo `app.py` serve como o controlador principal, conectando as funcionalidades dos outros módulos do sistema. Ele cuida da interação com o usuário, fornecendo as opções de cadastro, login e acesso às diferentes funcionalidades, como o banco de dados de circuitos e pilotos, e a loja da Mahindra Racing.
<br>
Fluxo de Interação:
Login/Cadastro: O usuário começa no menu de login/cadastro. Caso já tenha uma conta, faz login, senão pode se cadastrar.
Menu Principal: Após o login, o usuário é direcionado ao menu principal (que é gerido em outro arquivo), onde pode acessar as funções de banco de dados (para consultar informações de consumo energético) ou a Loja (para gastar seus EcoCoins).
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻

Essa seção implementa três mini-games temáticos.

```c
import random
from helpers import meu_index, limpar_tela
from game_dictionaries import dict_game_forca, perguntas_quiz, desafios_consumo
from cadastro_login import usuarios
```
Esta parte do código importa os módulos necessários.
<hr>

```c
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
```

Função `game_forca()`:
<ul>
    <li>Esta função implementa o jogo da Forca.</li>
    <li>O jogador tem 10 tentativas para adivinhar a palavra.</li>
    <li>O jogador insere uma letra e, se estiver correta, ela é revelada na posição correta na palavra.</li>
    <li>Se o jogador adivinhar todas as letras corretamente antes de esgotar as tentativas, ele vence o jogo.</li>
</ul>
<hr>

```c
def quiz_sustentavel(perguntas):
    print("Bem-vindo ao Quiz Sustentável!")
    pontuacao = 0
    perguntas_aleatorias = random.sample(list(perguntas.items()), len(perguntas))
    for pergunta, (opcoes, resposta_correta) in perguntas_aleatorias:
        print("\n" + pergunta)
        for i, opcao in enumerate(opcoes):
            print(opcao)
        while True:
            resposta = input("Escolha sua resposta (A-E): ").strip().upper()
            if resposta in "ABCDE":
                break
            else:
                print("Escolha inválida! Por favor, escolha uma das opções válidas: A, B, C, D, ou E.")
        if ord(resposta) - ord("A") == resposta_correta:
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
```

Este código implementa o Quiz Sustentável, um jogo interativo que avalia o conhecimento do jogador sobre sustentabilidade. Ele utiliza perguntas de múltipla escolha com respostas validadas. Abaixo segue uma explicação detalhada do funcionamento do código.
Função `quiz_sustentavel(perguntas)`:
<ul>
    <li>Apresentação do Quiz: Mostra uma mensagem de boas-vindas para o jogador.</li>
    <li>Sorteio de Perguntas: Usa a função random.sample para embaralhar a ordem das perguntas fornecidas.</li>
    <li>Iteração sobre as Perguntas: Exibe as perguntas e opções, captura a resposta do jogador e avalia se ela está correta ou errada.</li>
    <li>Validação da Resposta: Verifica se o jogador digitou uma resposta válida (A, B, C, D ou E).</li>
    <li>Pontuação: Atualiza a pontuação com base na precisão das respostas do jogador.</li>
    <li>Mensagem Final: Mostra uma mensagem de conclusão com o desempenho do jogador no quiz.</li>
</ul>
<hr>

```c
def desafio_consumo_sustentavel(desafios):
    print("Bem-vindo ao Desafio de Consumo Sustentável!")
    consumo_total = 0
    co2_total = 0
    desafios_aleatorios = random.sample(desafios, len(desafios))
    for desafio in desafios_aleatorios:
        print("\n" + desafio["descricao"])
        for i, (opcao, consumo, co2) in enumerate(desafio["opcoes"], start=1):
            print(f"{i}) {opcao} - Consumo: {consumo} kWh, Emissão de CO₂: {co2} kg")
        while True: 
            try:
                escolha = int(input("Escolha uma opção (1-3): ")) - 1  
                if 0 <= escolha < len(desafio["opcoes"]):  
                    break  
                else:
                    print("Escolha inválida! Por favor, escolha uma opção válida entre 1, 2 ou 3.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número entre 1 e 3.")
        consumo_escolhido, co2_escolhido = desafio["opcoes"][escolha][1], desafio["opcoes"][escolha][2]
        consumo_total += consumo_escolhido
        co2_total += co2_escolhido
        print(f"\nVocê escolheu: {desafio['opcoes'][escolha][0]}")
        print(f"Impacto desta escolha: {consumo_escolhido} kWh e {co2_escolhido} kg de CO₂.")
    print(f"\nDesafio concluído! Seu consumo total foi de {consumo_total:.2f} kWh e sua emissão de CO₂ foi de {co2_total:.2f} kg.")
    if consumo_total < 2:
        print("Parabéns! Você é um exemplo de sustentabilidade!")
    elif consumo_total < 4:
        print("Ótimo trabalho! Suas escolhas são bastante sustentáveis.")
    elif consumo_total < 6:
        print("Bom esforço! Mas há espaço para melhorar nas escolhas diárias.")
    else:
        print("Vamos continuar aprendendo sobre sustentabilidade para fazer escolhas mais conscientes no futuro.")
```

O código implementa o Desafio de Consumo Sustentável, um jogo interativo onde o jogador faz escolhas relacionadas ao consumo de energia e emissões de CO₂. Ele simula os impactos dessas decisões para conscientizar sobre práticas sustentáveis. Abaixo, está a explicação detalhada do código.
Função `desafio_consumo_sustentavel(desafios)`:
<ul>
    <li>Apresentação: Introduz o jogador ao desafio.</li>
    <li>Sorteio dos Cenários: As situações/desafios são apresentados em ordem aleatória.</li>
    <li>Exibição das Opções: Cada desafio possui opções com impactos associados.</li>
    <li>Validação da Escolha: Garante que o jogador selecione uma opção válida (1-3).</li>
    <li>Cálculo do Impacto: Soma os impactos de consumo de energia e emissões de CO₂ com base nas escolhas.</li>
    <li>Feedback Final: Exibe o impacto total do jogador e fornece mensagens motivacionais.</li>
</ul>
<hr>

```c
def games_menu(usuario):
    while True:
        print("Escolha um jogo:")
        for key, game in games.items():
            print(f"{key}. {game['name']}")
        choice = input("Digite o número da escolha: ")
        if choice == "0":  
            break
        elif choice in games:
            if games[choice]["game"]():
                play_again = input("Deseja jogar novamente? (s/n): ")
                if play_again.lower() == "s":
                    limpar_tela()
                    continue
                else:
                    if usuario['primeira_vez']:
                        usuario['primeira_vez'] = False
                        usuario['ECs'] += 1500
                        print(f"{usuario['username']}, por ter jogado pela primeira vez algum de nossos jogos, você receberá 1500 ECs de bônus")
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
                        print(f"{usuario['username']}, por ter jogado pela primeira vez algum de nossos jogos, você receberá 1500 ECs de bônus")
                    break
        else:
            print("Opção inválida. Tente novamente!")
    return
```

Loop Principal:
<ul>
    <li>Quando a função é chamada o código entra em um loop infinito, onde o jogador pode escolher qual jogo jogar.</li>
    <li>O jogador seleciona um jogo digitando o número correspondente.</li>
    <li>Após jogar um jogo, o jogador tem a opção de jogar novamente ou sair.</li>
    <li>Se for a primeira vez do usuário ganhando algum jogo ele recebe 1500 ECs de bônus.</li>
</ul>
<hr>

```c
games = {
    "1": {"name": "Eco Forca", "game": game_forca},
    "2": {"name": "Eco Quiz", "game": quiz_sustentavel, "args": perguntas_quiz},
    "3": {"name": "Desafio de Consumo", "game": desafio_consumo_sustentavel, "args": desafios_consumo},
    "0": {"name": "Sair"}
}
```

Dicionário de Jogos:
<ul>
    <li>Um dicionário chamado games é criado para associar cada jogo a um número.</li>
    <li>Cada jogo tem um nome e uma função associada.</li>
    <li>O usuário tem a opção de sair.</li>
</ul>

## Explicando o <a href="path">Código</a> 🧑‍💻
Essa seção implementa os dicionários de informações importantes usados para os minigames.
```c

dict_game_forca = {
    "words": [
        "SUSTENTABILIDADE", "ENERGIA", "SOLAR", "EOLICA", "RENOVAVEL", 
        "BIODIESEL", "HIDRELETRICA", "BIOMASSA", "FOTOVOLTAICO", "GEOTERMICA",
        "EFICIENCIA", "CONSUMO", "DESCARBONIZACAO", "RECICLAGEM", "TERMICA",
        "SUSTENTAVEL", "ECOSSISTEMA", "CONSERVACAO", "INOVACAO", "BIODEGRADAVEL"
    ],
    
    "tips": [
        "Conceito que visa suprir necessidades atuais sem comprometer gerações futuras",
        "O que move o mundo e sustenta o modo de vida moderno",
        "Fonte de energia gerada a partir do sol",
        "Fonte de energia gerada a partir do vento",
        "Tipo de energia que não se esgota",
        "Combustível produzido a partir de fontes renováveis como óleos vegetais",
        "Fonte de energia gerada a partir da força da água",
        "Tipo de energia obtida a partir de matéria orgânica",
        "Tipo de energia que usa células para converter luz solar em eletricidade",
        "Energia que utiliza o calor da Terra como fonte",
        "Capacidade de fazer mais com menos energia",
        "Quantidade de energia usada por equipamentos ou sistemas",
        "Processo de reduzir emissões de gases de efeito estufa",
        "Processo de reaproveitamento de materiais descartados",
        "Energia gerada pela queima de combustíveis",
        "Relativo a práticas que minimizam impacto ambiental",
        "Conjunto de organismos que interagem entre si e com o ambiente",
        "Prática de manter e proteger recursos naturais",
        "Introdução de novas tecnologias e métodos sustentáveis",
        "Material que se decompõe naturalmente sem poluir o ambiente"
    ]
}

perguntas_quiz = {
    "Qual é a fonte de energia renovável mais utilizada no Brasil?": 
    (["A) Solar", "B) Eólica", "C) Hidrelétrica", "D) Biomassa", "E) Nuclear"], 2),
    
    "Qual gás é o maior responsável pelo efeito estufa?": 
    (["A) Metano", "B) Dióxido de carbono", "C) Óxido nitroso", "D) Vapor de água", "E) Ozônio"], 1),
    
    "Qual destes hábitos ajuda a economizar energia em casa?": 
    (["A) Deixar as luzes acesas", "B) Usar aparelhos durante horários de pico", "C) Manter aparelhos em standby", 
      "D) Usar lâmpadas LED", "E) Aumentar a potência dos aparelhos"], 3),
    
    "Qual é o benefício do uso de energia solar?": 
    (["A) Reduz custos de eletricidade", "B) Aumenta as emissões de CO₂", "C) Gasta muita água", 
      "D) Produz resíduos tóxicos", "E) Causa poluição sonora"], 0),
    
    "Qual dessas energias é considerada não renovável?": 
    (["A) Solar", "B) Hidrelétrica", "C) Carvão", "D) Eólica", "E) Biomassa"], 2),
    
    "Qual a principal desvantagem da energia eólica?": 
    (["A) Elevado custo de instalação", "B) Emissão de CO₂", "C) Causa poluição das águas", 
      "D) Intermitência do vento", "E) Necessita de combustíveis fósseis"], 3),
    
    "Qual é uma vantagem do uso de carros elétricos?": 
    (["A) Baixa eficiência energética", "B) Menor autonomia", "C) Maior emissão de CO₂", 
      "D) Alta dependência de petróleo", "E) Menos emissões de poluentes"], 4),
    
    "Qual dessas é uma forma de reduzir o consumo de energia elétrica?": 
    (["A) Usar lâmpadas incandescentes", "B) Reduzir o uso de ar-condicionado", 
      "C) Manter todos os aparelhos ligados", "D) Aumentar a potência dos aparelhos", 
      "E) Usar eletrodomésticos antigos"], 1),
    
    "Qual energia renovável depende do movimento da água?": 
    (["A) Solar", "B) Eólica", "C) Biomassa", "D) Hidrelétrica", "E) Geotérmica"], 3),
    
    "Qual destes é um efeito do aquecimento global?": 
    (["A) Diminuição do nível do mar", "B) Resfriamento global", "C) Extinção de espécies", 
      "D) Aumento das calotas polares", "E) Estabilização do clima"], 2),
}

desafios_consumo = [
    {
        "descricao": "Você está em casa em um dia quente. Como deseja refrescar o ambiente?",
        "opcoes": [
            ("Ventilador ligado por 2 horas", 0.5, 0.1),
            ("Ar-condicionado no modo econômico por 1 hora", 1.5, 0.3),
            ("Ar-condicionado no modo máximo por 1 hora", 3, 0.7)
        ]
    },
    {
        "descricao": "Você precisa iluminar a sala à noite. Qual opção você escolhe?",
        "opcoes": [
            ("Lâmpadas LED ligadas por 4 horas", 0.4, 0.05),
            ("Lâmpadas fluorescentes por 4 horas", 0.6, 0.1),
            ("Lâmpadas incandescentes por 4 horas", 1.2, 0.3)
        ]
    },
    {
        "descricao": "Na cozinha, você está preparando uma refeição. Qual fonte de aquecimento você usa?",
        "opcoes": [
            ("Fogão a gás", 1.0, 0.2),
            ("Forno elétrico por 30 minutos", 1.8, 0.4),
            ("Micro-ondas por 10 minutos", 0.5, 0.1)
        ]
    },
    {
        "descricao": "Você precisa lavar roupas. Como vai realizar essa tarefa?",
        "opcoes": [
            ("Máquina de lavar em modo econômico", 0.5, 0.1),
            ("Máquina de lavar em modo normal", 1.0, 0.2),
            ("Lavar a mão e secar ao sol", 0.0, 0.0)
        ]
    },
    {
        "descricao": "Você vai ao trabalho. Qual meio de transporte você escolhe?",
        "opcoes": [
            ("Bicicleta", 0.0, 0.0),
            ("Carro elétrico", 0.3, 0.05),
            ("Carro a combustão", 1.5, 0.3)
        ]
    }
]

```
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻

Este módulo gerencia e apresenta dados relacionados ao consumo de energia, emissões de CO₂ e economia financeira por estado brasileiro. Os dados são carregados de um arquivo JSON (dados.json), e as funções fornecem diferentes formas de consulta e visualização.

```c
import json
import matplotlib.pyplot as plt
```

Importa os módulos `json` e `matplotlib`.
<hr>

```c
def carregar_dados(arquivo_json='dados.json'):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    return dados
```

Objetivo: Lê e carrega os dados do arquivo JSON.
Parâmetros:
<ul>
    <li>arquivo_json: Nome do arquivo JSON (padrão: dados.json).</li>
</ul>
Retorno: Dicionário com os dados carregados.
<hr>

```c
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
```

Objetivo: Exibe os dados detalhados de um estado específico.
Parâmetros:
<ul>
    <li>dados: Dicionário com os dados carregados.</li>
    <li>estado: Sigla do estado (ex: "SP", "RJ").</li>
</ul>
Descrição: Mostra métricas como consumo de energia, emissões de CO₂, consumo ideal e economia financeira. Sugere formas de economizar com base nos dados.
<hr>

```c
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
```

Objetivo: Cria um gráfico de barras com os dados do estado.
Parâmetros:
<ul>
    <li>dados: Dicionário com os dados carregados.</li>
    <li>estado: Sigla do estado.</li>
</ul>
Descrição: Exibe as métricas em um gráfico para melhor visualização. Usa as bibliotecas matplotlib.pyplot para criar o gráfico.
Gráfico Gerado:
<ul>
    <li>Métricas: Consumo de energia, emissões de CO₂, consumo ideal e economia financeira.</li>
    <li>Exemplo: Um gráfico de barras colorido comparando essas métricas.</li>
</ul>
<hr>

```c
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
```

Objetivo: Compara os dados de dois estados em um único gráfico.
Parâmetros:
<ul>
    <li>dados: Dicionário com os dados carregados.</li>
    <li>estado1: Sigla do primeiro estado.</li>
    <li>estado2: Sigla do segundo estado.</li>
</ul>
Descrição:
<ul>
    <li>Gera um gráfico de barras lado a lado comparando as métricas dos dois estados.</li>
    <li>Permite comparar métricas como consumo e economia financeira entre regiões.</li>
</ul>
<hr>

```c
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
```

Objetivo: Interface interativa para consultar dados dos estados.
Descrição:
<ul>
    <li>Permite que o usuário escolha um estado e visualize os dados detalhados.</li>
    <li>Oferece a opção de: Exibir um gráfico com os dados do estado; Comparar os dados com outro estado; Realizar novas consultas; Trata entradas inválidas de forma amigável.</li>
</ul>
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻
O arquivo JSON contém os dados por estado em formato estruturado. Cada estado possui as seguintes métricas:
<ul>
    <li>consumo_energia: Consumo médio de energia elétrica (em kW/h).</li>
    <li>co2_emissoes: Emissões de CO₂ (em megatoneladas).</li>
    <li>consumo_ideal: Consumo ideal de energia elétrica (em kW/h).</li>
    <li>economia_financeira: Economia financeira potencial (em milhares de reais).</li>
</ul>







## Explicando o <a href="path">Código</a> 🧑‍💻

Essa seção implementa uma loja virtual, onde os usuários podem comprar itens como canecas, camisetas e ingressos usando a moeda virtual Eco Coins (EC). 
<br>

```c
def produtos_disponiveis():
    print("\nProdutos disponíveis:")
    for id_produto, info in produtos.items():
        print(f"{id_produto} - {info['nome']} : {info['preco']} MCs (Estoque: {info['estoque']})")
```

Printa o catálogo de produtos da loja.
<hr>

```c
def adicionar_ao_carrinho(usuario, id_produto, quantidade):
    if id_produto not in usuario["carrinho"]:
        usuario["carrinho"][id_produto] = 0
    usuario["carrinho"][id_produto] += quantidade
```

Adiciona um produto ao carrinho de compras do usuário. Se o produto já estiver no carrinho, aumenta a quantidade.
<hr>

```c
def finalizar_compra(usuario):
    if not usuario["endereco"].get("estado"):
        print("Precisamos do seu endereço para concluir a compra.")
        estado = input("Digite seu Estado:\n--> ")
        rua = input("Digite sua rua:\n--> ")
        numero = input("Digite o número da residência:\n--> ")
        complemento = input("Digite o complemento (deixe em branco se não houver):\n--> ")
        cep = input("Digite seu CEP:\n--> ")
        usuario["endereco"] = {
            "estado": estado,
            "rua": rua,
            "numero": numero,
            "complemento": complemento,
            "cep": cep
        }
    total_compra = 0
    itens_comprados = []
    for id_produto, quantidade in usuario["carrinho"].items():
        preco = produtos[id_produto]["preco"]
        estoque = produtos[id_produto]["estoque"]
        if quantidade <= estoque:
            total_compra += quantidade * preco
            produtos[id_produto]["estoque"] -= quantidade
            itens_comprados.append((produtos[id_produto]["nome"], quantidade, preco))
        else:
            print(f"Quantidade de {produtos[id_produto]['nome']} insuficiente no estoque. Sua compra será ajustada.")
            usuario["carrinho"][id_produto] = estoque
            total_compra += estoque * preco
            produtos[id_produto]["estoque"] = 0
            itens_comprados.append((produtos[id_produto]["nome"], estoque, preco))
    if usuario["MCs"] >= total_compra:
        usuario["MCs"] -= total_compra
        usuario["saldo_compras"].append({"itens": itens_comprados, "total": total_compra})
        usuario["carrinho"] = {}  
        endereco = usuario["endereco"]
        print(f"Compra realizada com sucesso! Total: {total_compra} MCs")
        print(f"Seu pedido será enviado para:\n"
              f"{endereco['rua']}, {endereco['numero']} {endereco['complemento']}\n"
              f"{endereco['estado']} - CEP: {endereco['cep']}")
    else:
        print("Você não tem Mahindra Coins suficientes para esta compra.")
```

Caso o usuário não tenha um endereço cadastrado ele é obrigado a preencher todos os campos e após isso finaliza-se a compra dos produtos no carrinho do usuário. Verifica se a quantidade de itens no carrinho está disponível no estoque, ajusta o carrinho se necessário e atualiza o estoque.
Deduz o total da compra do saldo de Mahindra Coins (MCs) do usuário, esvaziando o carrinho após a compra.
<hr>

```c
def exibir_compras_passadas(usuario):
    if not usuario["saldo_compras"]:
        print("Nenhuma compra realizada.")
    else:
        for id, compra in enumerate(usuario["saldo_compras"], start=1):
            print(f"\nCompra {id}:")
            for item in compra["itens"]:
                print(f"- Produto: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]} MCs /cada")
            print(f"Total da compra: {compra['total']} MCs")
        print(f"Saldo restante: {usuario['MCs']} MCs")
```

Exibe as compras passadas do usuário. Para cada compra, exibe os itens comprados, suas quantidades, preços e o total gasto, além de mostrar o saldo restante de MCs.
<hr>

```c
def adicionar_produto():
    id_produto = str(len(produtos) + 1)
    nome_produto = input("Digite o nome do novo produto:\n--> ")
    preco = float(input("Digite o preço do produto:\n--> "))
    estoque = int(input("Digite a quantidade em estoque:\n--> "))
    produtos[id_produto] = {"nome": nome_produto, "preco": preco, "estoque": estoque}
    print(f"Produto {nome_produto} adicionado com sucesso!")
```

Permite a um administrador adicionar um novo produto à loja, solicitando ID, nome, preço e estoque.
<hr>

```c
def modificar_produto():
    id_produto = input("Digite o ID do produto que deseja modificar o estoque:\n--> ")
    if id_produto in produtos:
        novo_estoque = int(input("Digite a nova quantidade em estoque:\n--> "))
        produtos[id_produto]["estoque"] = novo_estoque
        print(f"Estoque do produto {produtos[id_produto]['nome']} atualizado para {novo_estoque}.")
        novo_preco = float(input("Digite o novo preço:\n--> "))
        produtos[id_produto]["preco"] = novo_preco
        print(f"Preço do produto {produtos[id_produto]['nome']} atualizado para {novo_preco}.")
    else:
        print("Produto não encontrado.")
```

Permite a um administrador modificar o estoque e o preço de um produto existente.
<hr>

```c
def remover_produto():
    id_produto = input("Digite o ID do produto que deseja remover:\n--> ")
    if id_produto in produtos:
        nome_produto = produtos[id_produto]["nome"]
        del produtos[id_produto]
        print(f"Produto '{nome_produto}' removido com sucesso!")
        novos_produtos = {}
        for novo_id, dados in enumerate(produtos.values(), start=1):
            novos_produtos[str(novo_id)] = dados
        produtos.clear()
        produtos.update(novos_produtos)
    else:
        print("Produto não encontrado.")
```

Permite a um administrador remover um produto existente.
<hr>

```c
def admin_zone():
    opcao_crud_admin = ["adicionar", "modificar", "remover"]
    admin_opcao = forca_opcao("Você deseja adicionar, modificar ou remover produtos? (s/n):\n--> ", ['s', 'n'], "Opção inválida!").lower()
    if admin_opcao == 's':
        admin_action = forca_opcao("Digite 'adicionar' para adicionar produtos, 'modificar' para alterar produto existente e 'remover' para remover produto:\n--> ", 
                                    opcao_crud_admin, "Opção inválida").lower()
        if admin_action == "adicionar":
            adicionar_produto()
        elif admin_action == "modificar":
            modificar_produto()
        elif admin_action == "remover":
            remover_produto()
        produtos_disponiveis()
```

Área de funcionalidades de um administrador onde funções anteriormente mencionadas são chamadas dependendo com a escolha do administrador.
<hr>

```c
def loja(usuario):
    print(f"Bem-vindo à loja da Mahindra Racing, {usuario['username']}!")
    print(f"Seu saldo atual é: {usuario['MCs']} MCs")
    while True:
        produtos_disponiveis()
        if usuario["admin"]:
            admin_zone()
        escolha = input("Digite o ID do produto que deseja comprar, 'compras' para ver suas compras, ou 'sair' para sair:\n--> ").lower()
        if escolha == "sair":
            print("Saindo da loja...")
            return
        if escolha == "compras":
            exibir_compras_passadas(usuario)
            continue
        if escolha in produtos:
            try:
                quantidade = int(input(f"Quantas unidades de {produtos[escolha]['nome']} você deseja adicionar ao carrinho?\n--> "))
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")
                continue
            if quantidade <= produtos[escolha]["estoque"]:
                adicionar_ao_carrinho(usuario, escolha, quantidade)
                print(f"{quantidade} unidade(s) de {produtos[escolha]['nome']} adicionada(s) ao carrinho.")
            else:
                print("Quantidade em estoque insuficiente.")
        else:
            print("Produto não encontrado.")
            continue
        continuar = forca_opcao("Deseja continuar comprando? (s/n):\n--> ", ['s', 'n'], "Opção inválida!").lower()
        if continuar == 'n':
            finalizar_compra(usuario)
            break
```

Exibe a loja, mostrando os produtos disponíveis com seus respectivos preços e quantidades em estoque além de conter as funcionalidades dela. Se o usuário for um administrador, opções adicionais serão mostrados, como adicionar, modificar ou remover produtos.
<hr>

```c
produtos = {
    "1" : {"nome": "Caneca com a logo da Mahindra", "preco": 2000.0, "estoque": 50},
    "2" : {"nome": "Ingresso Formula E", "preco": 100000.0, "estoque": 3},
    "3" : {"nome": "Camiseta com a logo da Mahindra", "preco": 5000.0, "estoque": 15},
    "4" : {"nome": "Boné da escuderia Mahindra", "preco": 2500.0, "estoque": 25},
    "5" : {"nome": "Chaveiro com o símbolo da Mahindra", "preco": 500.0, "estoque": 100},
    "6" : {"nome": "Adesivo Mahindra Racing", "preco": 250.0, "estoque": 100}
}
```

Um dicionário que armazena o catálogo de produtos da loja virtual, onde as chaves são os IDs do respectivo produto, e os valores são outros dicionários contendo nome, preço e estoque do produto.
<hr>

<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
