from models.produtos import Produto


class LinhaBranca(Produto):
    comissao = 0.15

    def __init__(self, consumo, classificacao, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.consumo = consumo
        self.classificacao = classificacao
