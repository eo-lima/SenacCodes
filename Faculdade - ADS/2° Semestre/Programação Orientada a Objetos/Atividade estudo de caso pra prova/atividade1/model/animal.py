from model.usuario import *

class Animal:

    pets = []

    cachorros = []
    gatos = []

    def __init__(self, nome, peso: float, tutor: Tutor):
        self.nome = nome
        self.peso = peso
        self.tutor = tutor

class Cachorro(Animal):
    def __init__(self, raca, cor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.raca = raca
        self.cor = cor

class Gato(Animal):
    def __init__(self, cor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cor = cor