from model.Pessoa import *
from view.view import *

def control():
    while True:
        opcao = menu()
        if opcao == "1":
            dados = cadastrar()
            if dados["tipo"] == "cliente":
                cadastro = Cliente.cadastrar_cliente(dados)
                if cadastro == "sucesso":
                    cadastro_confirmado()
                else:
                    erro_cpf()
        elif opcao == "2":
            print("Listando...")
