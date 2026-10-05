from models.produtos import Produto


class Eletroportateis(Produto):
    comissao = 0.10

    def __init__(self, voltagem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voltagem = voltagem
