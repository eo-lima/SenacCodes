from autor import Autor
from editora import Editora

class Livro:
    def __init__(self, titulo, publicacao, paginas, quantidade, autor: Autor, editora: Editora):
        self.titulo = titulo
        self.publicacao = publicacao
        self.paginas = paginas
        self.quantidade = quantidade
        self.autor = autor
        self.editora = editora