from Subpessoas.cliente import Cliente
from Subpessoas.vendedor import Vendedor
from Subprodutos.audio import Audio
from Subprodutos.eletroportatil import Eletroportateis
from Subprodutos.linhabranca import LinhaBranca
from Subprodutos.video import Video
from estoque import Estoque
from venda import Venda
from pessoas import Pessoa

loop = True

while loop:
    print("=========================")
    print("==        \033[31mMENU\033[0m         ==")
    print("=========================")
    print("\033[32m1 - Cadastrar Usuário\033[0m")
    print("\033[32m2 - Listar Usuários\033[0m")
    print("\033[32m3 - Cadastrar Produto\033[0m")
    print("\033[32m4 - Listar Produtos\033[0m")
    print("\033[32m5 - Registrar Venda\033[0m")
    opcao = input("Digite a opção que deseja: ")
    match opcao:
        case "1":
            tipo_de_usuario = input("Qual tipo de usuário deseja cadastrar? (1 - Cliente, 2 - Vendedor)\n")
            if tipo_de_usuario == "1":
                nome = input("Digite o nome do cliente: ")
                while True:
                    try:
                        cpf = int(input("Digite o CPF do cliente: "))
                        break
                    except ValueError:
                        print("Digite apenas números.")
                        continue
                cliente = Cliente(nome, cpf)
                Pessoa.clientes.append(cliente)
                print("\033[32mCliente cadastrado!\033[0m")
            elif tipo_de_usuario == "2":
                nome = input("Digite o nome do vendedor: ")
                while True:
                    try:
                        cpf = int(input("Digite o CPF do vendedor: "))
                        break
                    except ValueError:
                        print("Digite apenas números.")
                        continue
                vendedor = Vendedor(nome, cpf)
                Pessoa.vendedores.append(vendedor)
                print("\033[32mVendedor cadastrado!\033[0m")
            else:
                print("\033[31mOpção Inválida.\033[0m")
        case "2":
            listar = input("Qual tipo de usuário deseja listar? (1 - Clientes, 2 - Vendedores)\n")
            if listar == "1":
                print("\033[32mLista de Clientes: \033[0m\n")
                for cliente in Pessoa.clientes:
                    print(f"Nome: {cliente.nome}\nCPF: {cliente.cpf}\n")
            elif listar == "2":
                print("\033[32mLista de Vendedores: \033[0m\n")
                for vendedor in Pessoa.vendedores:
                    print(f"Nome: {vendedor.nome}\nCPF: {vendedor.cpf}\n")
        case "3":
            tipo_de_produto = input("Qual tipo de produto deseja cadastrar?\n(1 - Áudio, 2 - Eletroportátil, 3 - Linha Branca, 4 - Vídeo)\n")
            if tipo_de_produto == "1":
                Audio.cadastrar_produto()
            elif tipo_de_produto == "2":
                Eletroportateis.cadastrar_produto()
            elif tipo_de_produto == "3":
                LinhaBranca.cadastrar_produto()
            elif tipo_de_produto == "4":
                Video.cadastrar_produto()
            else:
                print("\033[31mOpção Inválida.\033[0m")
        case "4":
            Estoque.listar_produtos()
        case "5":
            Venda.realizar_venda()
