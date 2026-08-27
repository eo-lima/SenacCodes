class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nota1, nota2, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    def __init__(self, materia, cargahoraria, salario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.materia = materia
        self.cargahoraria = cargahoraria
        self.salario = salario

    def dar_aula(self):
        print(f"O professor {self.nome} está dando aula de {self.materia}.")


professor = Professor("Matemática", 30, 15000, "Enzo", 18)
professor.dar_aula()
aluno = Aluno(10,8, "Enzo", 18)