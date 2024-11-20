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
