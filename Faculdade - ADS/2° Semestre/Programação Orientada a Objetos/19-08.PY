def media(*args):
    soma = 0
    for i in args:
        soma += i
    media = soma/(len(args))
    return media

print(media(2, 5, 10))

def concatenar(*args):
    superpalavra = ""
    for i in args:
        superpalavra += i
    return superpalavra

print(concatenar("A","B"))

def maior_valor(*args):
    maior_valor = 0
    for i in range(len(args)):
        if args[i] > maior_valor:
            maior_valor = args[i]
    return maior_valor

print(maior_valor(1, 5, 3, 10, 8))

def cadastrar_produto(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    print("Produto cadastrado com sucesso.")

cadastrar_produto(nome="Macarrão", preco=6.00, marca="Dona Maria", validade="03/10")

def resumo_pessoa(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

resumo_pessoa(nome="Enzo", idade=18, cidade="Campo Grande", altura=1.67)
    
    