from helpers import forca_opcao

def produtos_disponiveis():
    print("\nProdutos disponíveis:")
    for id_produto, info in produtos.items():
        print(f"{id_produto} - {info['nome']} : {info['preco']} ECs (Estoque: {info['estoque']})")

def adicionar_ao_carrinho(usuario, id_produto, quantidade):
    if id_produto not in usuario["carrinho"]:
        usuario["carrinho"][id_produto] = 0
    usuario["carrinho"][id_produto] += quantidade

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
    if usuario["ECs"] >= total_compra:
        usuario["ECs"] -= total_compra
        usuario["saldo_compras"].append({"itens": itens_comprados, "total": total_compra})
        usuario["carrinho"] = {}  
        endereco = usuario["endereco"]
        print(f"Compra realizada com sucesso! Total: {total_compra} ECs")
        print(f"Seu pedido será enviado para:\n"
              f"{endereco['rua']}, {endereco['numero']} {endereco['complemento']}\n"
              f"{endereco['estado']} - CEP: {endereco['cep']}")
    else:
        print("Você não tem EcoSpheresuficientes para esta compra.")

def exibir_compras_passadas(usuario):
    if not usuario["saldo_compras"]:
        print("Nenhuma compra realizada.")
    else:
        for id, compra in enumerate(usuario["saldo_compras"], start=1):
            print(f"\nCompra {id}:")
            for item in compra["itens"]:
                print(f"- Produto: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]} ECs /cada")
            print(f"Total da compra: {compra['total']} ECs")
        print(f"Saldo restante: {usuario['ECs']} ECs")
    
def adicionar_produto():
    id_produto = str(len(produtos) + 1)
    nome_produto = input("Digite o nome do novo produto:\n--> ")
    preco = float(input("Digite o preço do produto:\n--> "))
    estoque = int(input("Digite a quantidade em estoque:\n--> "))
    produtos[id_produto] = {"nome": nome_produto, "preco": preco, "estoque": estoque}
    print(f"Produto {nome_produto} adicionado com sucesso!")

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

def loja(usuario):
    print(f"Bem-vindo à loja da EcoSphere, {usuario['username']}!")
    print(f"Seu saldo atual é: {usuario['ECs']} ECs")
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

produtos = {
    "1" : {"nome": "Caneca com a logo da EcoSphere", "preco": 2000.0, "estoque": 50},
    "2" : {"nome": "Ingresso Formula E", "preco": 100000.0, "estoque": 3},
    "3" : {"nome": "Camiseta com a logo da EcoSphere", "preco": 5000.0, "estoque": 15},
    "4" : {"nome": "Boné da escuderia EcoSphere", "preco": 2500.0, "estoque": 25},
    "5" : {"nome": "Chaveiro com o símbolo da EcoSphere", "preco": 500.0, "estoque": 100},
    "6" : {"nome": "Adesivo EcoSphere Racing", "preco": 250.0, "estoque": 100}
}
