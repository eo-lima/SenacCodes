class Estoque:
     
    lista_audio = []
    lista_eletroportatil = []
    lista_linhabranca = []
    lista_video = []

    def listar_produtos():
        tipo_de_produto = input("Qual tipo de produto deseja listar? (1 - Audio, 2 - Eletroportatil, 3 - Linha Branca, 4 - Vídeo)")
        if tipo_de_produto == "1":
            for audio in Estoque.lista_audio:
                print(f"Nome: {audio._nome}\nPreço: R${audio._preco}\nQuantidade: {audio._quantidade}\nGarantia: {audio._garantia} dias\n")
        elif tipo_de_produto == "2":
            for e in Estoque.lista_eletroportatil:
                print(f"Nome: {e._nome}\nPreço: R${e._preco}\nQuantidade: {e._quantidade}\nGarantia: {e._garantia} dias\nVoltagem: {e.voltagem}\n")
        elif tipo_de_produto == "3":
            for lb in Estoque.lista_linhabranca:
                print(f"Nome: {lb._nome}\nPreço: R${lb._preco}\nQuantidade: {lb._quantidade}\nGarantia: {lb._garantia} dias\nConsumo: {lb.consumo}\nClassificação: {lb.classificacao}\n")
        elif tipo_de_produto == "4":
            for v in Estoque.lista_video:
                print(f"Nome: {v._nome}\nPreço: R${v._preco}\nQuantidade: {v._quantidade}\nGarantia: {v._garantia}\n")
        else:
            print("\033[31mOpção Inválida.\033[0m")