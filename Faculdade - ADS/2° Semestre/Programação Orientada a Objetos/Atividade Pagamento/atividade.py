class Pagamento:
    def __init__(self, pagamento: float):
        self.pagamento = pagamento

    def processar_pagamento(self):
        print("Pagamento realizado com sucesso!")

    def resumo_pagamento(self):
        print("RESUMO DA COMPRA:\n")
        print(f"Valor original: R${self.pagamento}")
        print(f"Forma de Pagamento: Cartão de Débito")
        print(f"Descontos: Não aplicado.")
        print(f"Acréscimos: Não aplicado.")
        print(f"Valor de parcelas: Não aplicado.")
        print(f"Valor total a ser pago: R${self.pagamento}")

class PagamentoCredito(Pagamento):
    def __init__(self, pagamento, parcelas):
        super().__init__(pagamento)
        self.pagamento = pagamento
        self.parcelas = parcelas

    def processar_pagamento(self):
        print("Pagamento realizado com sucesso.")

    def resumo_pagamento(self):
        acrescimos = self.pagamento/10
        valortotal = self.pagamento + acrescimos
        parcelas = valortotal/self.parcelas
        print(f"RESUMO DA COMPRA\n")
        print(f"Valor original: R${self.pagamento}")
        print(f"Forma de Pagamento: Cartão de Crédito")
        print(f"Descontos: Não aplicado.")
        print(f"Acrécimos: R${acrescimos}")
        print(f"Valor de parcela: R${parcelas}")
        print(f"Valor total a ser pago: R${valortotal}")

class PagamentoPix(Pagamento):
    def __init__(self, pagamento: float):
        super().__init__(pagamento)
        self.pagamento = pagamento

    def processar_pagamento(self):
        print("Pagamento realizado com sucesso.")

    def resumo_pagamento(self):
        decrescimos = (self.pagamento*5)/100
        valortotal = self.pagamento - decrescimos
        print(f"RESUMO DA COMPRA\n")
        print(f"Valor original: R${self.pagamento}")
        print(f"Forma de pagamento: Pix")
        print(f"Descontos: R${decrescimos}")
        print(f"Acréscimos: Não aplicado.")
        print(f"Valor de parcela: Não aplicado")
        print(f"Valor total a ser pago: R${valortotal}")

class PagamentoDebito(Pagamento):
    def __init__(self, pagamento):
        super().__init__(pagamento)
        self.pagamento = pagamento

    def processar_pagamento(self):
        print("Pagamento realizado com sucesso.")

    def resumo_pagamento(self):
        return super().resumo_pagamento()

while True:   
    print("===============")
    print("      MENU     ")
    print("===============")
    opcao = input("1 - Realizar pagamento no crédito\n2 - Realizar pagamento no débito\n3 - Realizar pagamento no pix\n4 - Sair\nDigite a opção que deseja: ")
    match opcao:
        case "1":
            valor = float(input("Digite o valor que será pago: "))
            while True:
                parcela = int(input("Digite o número de parcela (de 1 a 10): "))
                if parcela < 1 or parcela > 10:
                    print("Número inválido de parcelas.")
                    continue
                else:
                    break
            pagamento = PagamentoCredito(valor, parcela)
            pagamento.resumo_pagamento()
            confirmar = input("Deseja confirmar o pagamento? 1 - Sim, 2 - Não: ")
            if confirmar == "1":
                pagamento.processar_pagamento()
                continue
            else:
                continue
        case "2":
            valor = float(input("Digite o valor que será pago: "))
            pagamento = PagamentoDebito(valor)
            pagamento.resumo_pagamento()
            confirmar = input("Deseja confirmar o pagamento? 1 - Sim, 2 - Não: ")
            if confirmar == "1":
                pagamento.processar_pagamento()
                continue
            else:
                continue
        case "3":
            valor = float(input("Digite o valor que será pago: "))
            pagamento = PagamentoPix(valor)
            pagamento.resumo_pagamento()
            confirmar = input("Deseja confirmar o pagamento? 1 - Sim, 2 - Não: ")
            if confirmar == "1":
                pagamento.processar_pagamento()
                continue
            else:
                continue
        case "4":
            print("Saindo...")
            break
        

            
