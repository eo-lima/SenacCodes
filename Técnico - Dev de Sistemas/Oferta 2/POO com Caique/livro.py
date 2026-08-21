class Livro:
    def __init__(self, paginas, titulo, autor, genero, editora):
        self.paginas = paginas
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editora = editora
    
    def emprestar(self):
        Leitor.livros_emprestados.append(self)
    
class Leitor:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = []
    
    def pegar_emprestado(self, livro):
        livro.emprestar(self)


livro = Livro(10, "Enzao", "Enzo", "Bibliografia", "Editora do Enzo")
print(livro.titulo)