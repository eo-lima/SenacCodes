from autor import Autor
from editora import Editora

class Livro:
    def __init__(self, titulo, publicacao, paginas, quantidade, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.publicacao = publicacao
        self.paginas = paginas
        self.quantidade = quantidade
        self.autor = autor
        self.editora = editora