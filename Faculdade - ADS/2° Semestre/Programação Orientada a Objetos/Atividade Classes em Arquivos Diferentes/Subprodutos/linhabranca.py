from produtos import Produto

class LinhaBranca(Produto):
    def __init__(self, consumo, classificacao, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.consumo = consumo
        self.classificacao = classificacao