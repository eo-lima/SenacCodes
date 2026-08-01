class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = [] #Uma turma pode haver vários alunos.
    
    def inserir_aluno(self, aluno : Aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print("Aluno:", aluno.nome) #Acessando o atributo nome da classe (objeto) aluno!
			
ana = Aluno("Ana Maria")
joao = Aluno("João Fulano")

turma = Turma("ADS")
turma.inserir_aluno(ana) #Adicionando os alunos na turma
turma.inserir_aluno(joao)

turma.listar_alunos() #Mostrando todos os alunos