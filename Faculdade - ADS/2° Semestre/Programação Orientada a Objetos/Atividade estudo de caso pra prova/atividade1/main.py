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
                elif dados["tipo"] == "gato":
                    controller.cadastrar_gato(dados)
                elif dados["tipo"] == "veterinario":
                    controller.cadastrar_veterinario(dados)
        if opcao == "2":
            usuario = escolher_usuario()
            if usuario == "1":
                tutores = controller.listar_tutores()
                listar_tutores_view(tutores)
            if usuario == "2":
                pets = controller.listar_pets()
                listar_pets_view(pets)
            if usuario == "3":
                veterinarios = controller.listar_veterinarios()
                listar_veterinario_view(veterinarios)

            
