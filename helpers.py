def limpar_tela(linhas=10):
    print("\n" * linhas)

def forca_opcao(msg, opcoes, msg_erro):
    opcao = input(msg)
    while opcao not in opcoes:
        limpar_tela()
        print(msg_erro)
        opcao = input(msg)
    return opcao

def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False

def verifica_numero(msg, msg_erro):
    while True:
        num = input(msg)
        if num.isdigit():
            return int(num)
        print(msg_erro)

def print_de_opcoes(lista, line_break=True):
    output = '\n'.join([f'- {item}' for item in lista]) if line_break else ', '.join(lista)
    print(output)
    return output
