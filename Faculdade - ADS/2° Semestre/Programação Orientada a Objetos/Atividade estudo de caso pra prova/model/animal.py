from model.usuario import *

class Animal:

    cachorros = []

    def __init__(self, nome, peso: float, tutor: Tutor):
        self.nome = nome
        self.peso = peso
        self.tutor = tutor

class Cachorro(Animal):
    def __init__(self, raca, cor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.raca = raca
        self.cor = cor