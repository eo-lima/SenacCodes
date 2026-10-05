class ConsoleView:
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    RESET = "\033[0m"

    def exibir_menu(self):
        print("=========================")
        print(f"==        {self.VERMELHO}MENU{self.RESET}         ==")
        print("=========================")
        print(f"{self.VERDE}1 - Cadastrar Usuário{self.RESET}")
        print(f"{self.VERDE}2 - Listar Usuários{self.RESET}")
        print(f"{self.VERDE}3 - Cadastrar Produto{self.RESET}")
        print(f"{self.VERDE}4 - Listar Produtos{self.RESET}")
        print(f"{self.VERDE}5 - Registrar Venda{self.RESET}")
        print(f"{self.VERDE}6 - Exibir Comissão do Vendedor{self.RESET}")
        print(f"{self.VERDE}7 - Histórico de Compras do Cliente{self.RESET}")
        print(f"{self.VERDE}8 - Devolução e troca{self.RESET}")
        print(f"{self.VERDE}9 - Sair{self.RESET}")
        return input("Digite a opção que deseja: ")

    def digitar_texto(self, mensagem):
        return input(mensagem)

    def digitar_inteiro(self, mensagem, minimo=None):
        while True:
            try:
                valor = int(input(mensagem))
                if minimo is not None and valor < minimo:
                    print(f"{self.VERMELHO}Digite um valor maior ou igual a {minimo}.{self.RESET}")
                    continue
                return valor
            except ValueError:
                print("Digite apenas números.")

    def digitar_decimal(self, mensagem):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Digite apenas números.")

    def escolher_tipo_usuario(self):
        return input(
            "Qual tipo de usuário deseja cadastrar? "
            "(1 - Cliente, 2 - Vendedor)\n"
        )

    def escolher_tipo_listagem(self):
        return input(
            "Qual tipo de usuário deseja listar? "
            "(1 - Clientes, 2 - Vendedores)\n"
        )

    def escolher_tipo_produto(self, cadastro):
        if cadastro:
            return input(
                "Qual tipo de produto deseja cadastrar?\n"
                "(1 - Áudio, 2 - Eletroportátil, 3 - Linha Branca, 4 - Vídeo)\n"
            )
        return input(
            "Qual tipo de produto deseja listar? "
            "(1 - Áudio, 2 - Eletroportátil, 3 - Linha Branca, 4 - Vídeo)\n"
        )

    def mostrar_mensagem(self, mensagem, cor=None):
        cor_ansi = self.VERDE if cor == "verde" else self.VERMELHO if cor else ""
        reset = self.RESET if cor else ""
        print(f"{cor_ansi}{mensagem}{reset}")

    def listar_pessoas(self, titulo, pessoas):
        print(f"{self.VERDE}Lista de {titulo}: {self.RESET}\n")
        for pessoa in pessoas:
            print(f"Nome: {pessoa.nome}\nCPF: {pessoa.cpf}\n")

    def listar_produtos(self, produtos, tipo):
        for produto in produtos:
            detalhes = (
                f"Nome: {produto._nome}\n"
                f"Preço: R${produto._preco}\n"
                f"Quantidade: {produto._quantidade}\n"
                f"Garantia: {produto._garantia} dias\n"
            )
            if tipo == "2":
                detalhes += f"Voltagem: {produto.voltagem}\n"
            elif tipo == "3":
                detalhes += (
                    f"Consumo: {produto.consumo}\n"
                    f"Classificação: {produto.classificacao}\n"
                )
            print(f"{detalhes}\n")

    def mostrar_comissao(self, vendedor):
        print(f"Comissão de {vendedor.nome}: R${vendedor._comissao}")

    def mostrar_historico_compras(self, cliente):
        print(f"Histórico de Compras de {cliente.nome}: ")
        for produtos, valor_total in cliente.compras:
            for indice, item in enumerate(produtos, start=1):
                print(
                    f"Produto ({indice}): {item['produto']._nome}, "
                    f"Quantidade: {item['quantidade']}, "
                    f"Disponível para devolução/troca: "
                    f"{item.get('quantidade_disponivel', 0)}"
                )
            print(f"Valor Total: R${valor_total}\n")

    def mostrar_itens_elegiveis(self, itens):
        print("Produtos dentro do prazo de garantia:")
        for indice, (_, item) in enumerate(itens, start=1):
            data_venda = item["data_venda"].strftime("%d/%m/%Y")
            print(
                f"{indice} - {item['produto']._nome} | "
                f"Compra: {data_venda} | "
                f"Disponível: {item['quantidade_disponivel']}"
            )

    def escolher_operacao_devolucao(self):
        return input(
            "Escolha: (1 - Devolver, 2 - Trocar pelo mesmo produto)\n"
        )

    def adicionar_mais_produtos(self):
        return input(
            "Deseja adicionar mais um produto a compra? (1 - Sim, 2 - Não)"
        )

    def escolher_forma_pagamento(self):
        return input(
            "Qual será a forma de pagamento? (1 - A vista, 2 - Parcelado)"
        )

    def confirmar_compra(self):
        return input("Confirmar Compra? (1 - Sim, 2 - Não)")

    def mostrar_resumo_venda(
        self, produtos, subtotal, valor_total=None, parcelas=None
    ):
        print(f"{self.VERDE}Informações da Compra: {self.RESET}\n")
        print("Produtos:\n")
        for item in produtos:
            print(
                f"Produto: {item['produto']._nome}\n"
                f"Quantidade: {item['quantidade']}\n"
            )
        if parcelas is None:
            total = subtotal if valor_total is None else valor_total
            print(f"Valor Total: R${total}\n")
        else:
            print(f"Sub-total: R${subtotal}\n")
            print(f"Acréscimo: R${valor_total - subtotal}")
            print(
                f"Valor de cada parcela ({parcelas}): "
                f"R${valor_total / parcelas}"
            )
            print(f"Valor Total: R${valor_total}")
