#Atividade 1

class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print("O filme está sendo exibido.")

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def explodir():
        print("EXPLOSÃOOO")

class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def chorar(self):
        print("chorandooo")

class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def tensao(self):
        print("seloco mó tensao")

#Atividade 2

class Pessoa:
    def __init__(self, nome, idade):
        self.nome == nome
        self.idade == idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota1, nota2):
        super().__init__(nome, idade)
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return ((self.nota1 + self.nota2)/2)

    def situacao(self):
        if Aluno.calcular_media >= 6:
            return "Aprovado"
        elif Aluno.calcular_media < 6 and Aluno.calcular_media >= 4:
            return "Recuperação"
        else:
            return "Reprovado"

class Professor(Pessoa):
    def __init__(self, nome, idade, materia, cargahoraria, salario):
        super().__init__(nome, idade)
        self.materia = materia
        self.cargahoraria = cargahoraria
        self.salario = salario

    def dar_aula(self):
        print(f"O professor {self.nome} está dando aula de {self.materia}.")

# Atividade 3

class Ingresso:
    def __init__(self, preco: float, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self):
        novopreco = float(input("Digite o novo preço do ingresso: "))
        self.preco = novopreco
        print("Preço alterado com sucesso.")

    def mostrar_setor(self):
        return self.setor

class IngressoVIP(Ingresso):
    def __init__(self, preco: float, setor, camarote: bool, open_bar: bool, open_food: bool, estacionamento: bool):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar == True:
            print("Bebida pega")
        else:
            print("Open Bar fechado.")

    def acessar_camarote(self):
        if self.camarote == True:
            print("Camarote acessado")
        else:
            print("Camarote fechado.")

# Atividade 4
    
class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self):
        novopreco = float(input("Digite o novo preço da passagem: "))
        self.preco = novopreco
        print("Preço alterado com sucesso.")

    def escolher_assento(self):
        assento = input("Digite o assento que deseja (ex: A1): ")
        print(f"Assento escolhido: {assento}")

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print("Onibus abastecido.")

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaodeeembarque, checkin):
        super().__init__(preco, assento)
        self.portaodeembarque = portaodeeembarque
        self.checkin = checkin

    def decolar(self):
        print("Avião decolando...")

# Atividade 5

class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar():
        print("Negociandoo")

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def negociar(self):
        return super().negociar

    def mostrar_cpf(self):
        return self.cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def negociar(self):
        return super().negociar()

    def mostrar_cnpj(self):
        return self.cnpj

# Atividade 6

class Funcionario():
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self):
        ponto = int(input("Bateu ponto?"))
        if ponto == 1:
            self.pontos.append(1)
            return True
        else:
            self.pontos.append(0)
            return False


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def bater_ponto(self):
        return super().bater_ponto()

    def bater_meta(self):
        print("Parabéns, sua meta foi batida !!")

    def comissao(self):
        print("Comissão recebida !!")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def bater_ponto(self):
        return super().bater_ponto()

    def senha(self):
        senha = "admin123"
        senhagerente = input("Digite a senha: ")
        if senhagerente == senha:
            print("Senha correta !!")
        else:
            print("Senha incorreta !!")

# Atividade 7

class Brinquedos:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}")

class Carrinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou andando com {self.nome}")

class Bola(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou jogando bola com {self.nome}")

class Pelucia(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar():
        return super().brincar()

class Aviaozinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou jogando o meu {self.nome}")

class Dinossauro(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()

class Piao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou rodando o meu {self.nome}")

class CuboMagico(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou montando meu {self.nome}")

class Ioio(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou soltando meu {self.nome}")

class Patins(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou andando de {self.nome}")

class Corda(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        print(f"Estou pulando {self.nome}")

# Atividade 8

class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        return self.iptu

    def set_valor_aluguel(self):
        aluguel = float(input("Digite o novo valor do aluguel: R$"))
        self.valor_aluguel = aluguel
        print("Valor alterado !")

class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, piscina, sala_de_estar, churrasqueira, area_ao_quadrado, area_de_lazer, quartos):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.churrasqueira = churrasqueira
        self.area_ao_quadrado = area_ao_quadrado
        self.area_de_lazer = area_de_lazer
        self.quartos = quartos

    def obter_parcela_iptu(self):
        return super().obter_parcela_iptu()

    def set_valor_aluguel(self):
        return super().set_valor_aluguel()

class Condominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, piscina, churrasqueira, area_ao_quadrado, elevador, area_de_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.piscina = piscina
        self.churrasqueira = churrasqueira
        self.area_ao_quadrado = area_ao_quadrado
        self.area_de_lazer = area_de_lazer

    def obter_parcela_iptu(self):
        return super().obter_parcela_iptu()

    def set_valor_aluguel(self):
        return super().set_valor_aluguel()

class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, sala_de_estar, quartos, churrasqueira, area_ao_quadrado):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.sala_de_estar = sala_de_estar
        self.churrasqueira = churrasqueira
        self.area_ao_quadrado = area_ao_quadrado
        self.quartos = quartos

    def obter_parcela_iptu(self):
        return super().obter_parcela_iptu()

    def set_valor_aluguel(self):
        return super().set_valor_aluguel()

class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_ao_quadrado):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_ao_quadrado = area_ao_quadrado

    def obter_parcela_iptu(self):
        return super().obter_parcela_iptu()

    def set_valor_aluguel(self):
        return super().set_valor_aluguel()

class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, piscina, sala_de_estar, quartos, churrasqueira, area_ao_quadrado, area_de_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.churrasqueira = churrasqueira
        self.area_ao_quadrado = area_ao_quadrado
        self.area_de_lazer = area_de_lazer
        self.quartos = quartos

    def obter_parcela_iptu(self):
        return super().obter_parcela_iptu()

    def set_valor_aluguel(self):
        return super().set_valor_aluguel()

# Atividade 9

class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = (self.valor*17)/100
        frete = (self.valor*5)/100
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class Avista(Compra):
    def __init__(self, numero, produto, valor):
        super().__init__(numero, produto, valor)
        self.desconto = (self.valor*10)/100

    def calcular_valor_total(self):
        icms = (self.valor*17)/100
        frete = (self.valor*5)/100
        self.valor_total = (self.valor + icms + frete) - self.desconto
        return self.valor_total

class Parcelado(Compra):
    def __init__(self, numero, produto, valor, parcelas):
        super().__init__(numero, produto, valor)
        self.parcelas = parcelas

    def calcular_valor_total(self):
        icms = (self.valor*17)/100
        frete = (self.valor*5)/100
        self.valor_total = (self.valor + icms + frete)/self.parcelas
        return f"{self.parcelas} parcelas de R${self.valor_total}"

# Atividade 10

class Transporte:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Aquatico(Transporte):
    def __init__(self, capacidade, helices):
        super().__init__(capacidade)
        self.helices = helices

    def mover(self):
        print("O transporte está se movendo na água !")

class Submarino(Aquatico):
    def __init__(self, capacidade, helices, cor):
        super().__init__(capacidade, helices)
        self.cor = cor

    def mover(self):
        return super().mover()
    
class Cruzeiro(Aquatico):
    def __init__(self, capacidade, helices, cor):
        super().__init__(capacidade, helices)
        self.cor = cor

    def mover(self):
        return super().mover()

class Terrestre(Transporte):
    def __init__(self, capacidade, rodas):
        super().__init__(capacidade)
        self.rodas = rodas

    def mover(self):
        print("O transporte está se movendo na terra !")

class Carro(Terrestre):
    def __init__(self, capacidade, rodas, cor, portas, placa):
        super().__init__(capacidade, rodas)
        self.cor = cor
        self.portas = portas
        self.placa = placa

    def mover(self):
        return super().mover()

class Moto(Terrestre):
    def __init__(self, capacidade, rodas, cor, placa):
        super().__init__(capacidade, rodas)
        self.cor = cor
        self.placa = placa

    def mover(self):
        return super().mover()

moto = Moto(2, 2, "Vermelha", "AA0000")
moto.mover()



    
        

    