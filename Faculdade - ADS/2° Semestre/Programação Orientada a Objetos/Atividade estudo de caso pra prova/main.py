from controller import controller
from view.view import *

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            dados = cadastrar()
            if dados is not None:
                if dados["tipo"] == "tutor":
                    controller.cadastrar_tutor(dados)
                elif dados["tipo"] == "cachorro":
                    controller.cadastrar_cachorro(dados)
                elif dados["tipo"] == "veterinario":
                    controller.cadastrar_veterinario(dados)
            
