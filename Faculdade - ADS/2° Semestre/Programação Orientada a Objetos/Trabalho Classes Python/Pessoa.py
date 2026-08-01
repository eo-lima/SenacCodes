class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrarNome(self):
        return self.nome
    
    def alterarIdade(self):
        novaidade = input("Digite a nova idade: ")
        self.idade = novaidade
        print("Idade alterada com sucesso!")

    def imprimirEndereco(self):
        return self.endereco

class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self):
        novaeditora = input("Digite a nova editora: ")
        self.editora = novaeditora
        print("Editora alterada com sucesso")

    def listar_paginas(self):
        return self.paginas

class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrar_situacao(self):
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4)/4
        if self.media >= 7:
            return f"O aluno está APROVADO."
        elif self.media < 7 and self.media >= 5:
            return f"O aluno está de EXAME"
        else:
            return f"O aluno está REPROVADO."

class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self):
        deposito = float(input("Digite o valor que deseja depositar na sua conta: "))
        self.saldo = self.saldo + deposito
        print("Depósito realizado com sucesso.")

    def sacar(self):
        sacar = float(input("Digite o valor que deseja sacar da sua conta: "))
        if sacar > self.saldo:
            print("Não é possível sacar um valor acima do seu saldo.")
        else:
            self.saldo = self.saldo - sacar
            print("Saque realizado com sucesso.")

    def imprimir_saldo(self):
        return f"Seu saldo atual é de R${self.saldo}."

class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        return f"Nome completo: {self.nome} {self.sobrenome}"

    def calcular_salario(self):
        return f"R${self.valor_hora*self.horas_trabalhadas}"

    def incrementar_horas(self):
        incrementar = int(input("Quantas horas deseja incrementar?"))
        self.horas_trabalhadas = self.horas_trabalhadas + incrementar
        print("Horas incrementadas com sucesso!")

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def valor_raio(self):
        return self.raio

    def calcular_area(self):
        return (3.14*(self.raio**2))

    def calcular_circunferencia(self):
        return 2 * 3,14 * self.raio

class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
        self.anotacoes = []

    def validar_data(self):
        if self.mes < 1 or self.mes > 12:
            print("Mês inválido.")
            return False
        else:
            if self.mes == 2 and self.dia > 28:
                print("Dia inválido")
                return False
            elif self.dia > 31 or self.dia < 1:
                print("Dia inválido")
                return False
            else:
                return True

    def anotar_tarefa(self):
        if self.validar_data() == False:
            return "Não é possível anotar uma tarefa nessa data."
        else:
            self.anotacoes.append(self.anotacao)
            return "Tarefa anotada com sucesso."

    def mostrar_anotacao(self, dia, mes, ano):
        if dia == self.dia and mes == self.mes and ano == self.ano:
            for i, self.anotacao in enumerate(self.anotacoes, start=1):
                print(f"Anotação {i}: {self.anotacao}\n")
        else:
            print("Nenhuma anotação para esse dia.")

class Triangulo:
    def __init__(self):
        self.ladoA = float(input("Digite o valor do lado A do triângulo:"))
        self.ladoB = float(input("Digite o valor do lado B do triângulo:"))
        self.ladoC = float(input("Digite o valor do lado C do triângulo:"))

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def maior_lado(self):
        self.lados = [self.ladoA, self.ladoB, self.ladoC]
        self.maiorlado = self.lados.index(max(self.lados))
        if self.maiorlado == 0:
            print(f"É o lado A, {self.lados[0]}")
        elif self.maiorlado == 1:
            print(f"É o lado B, {self.lados[1]}")
        else:
            print(f"É o lado C, {self.lados[2]}")

class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = 120.0

    def calcular_imc(self):
        self.imc = self.peso / (self.altura**2)
        return self.imc

    def obter_mensalidade(self):
        if self.idade > 18:
            return f"R${self.mensalidade}"
        else: 
            return f"R${self.mensalidade//2}"
    
class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = 0

    def abastecer(self, abastecer):
        self.nivel = self.nivel + abastecer
        print("Carro abastecido!")
        
    def andar(self, andar):
        self.nivel = self.nivel - andar
        print("Você andou!")

    def mostrar_nivel(self):
        return self.nivel

    def calcular_imposto(self):
        imposto = self.valor * 0.025
        print(f"O imposto é de R${imposto}")
        return imposto

