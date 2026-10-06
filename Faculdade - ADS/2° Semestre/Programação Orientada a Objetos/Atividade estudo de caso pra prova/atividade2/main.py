from view.view import *

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            dados = cadastrar()
            if dados["tipo"] == "cliente":
                print("Cadastrando cliente...")