from produtos import Produto

class Eletroportateis(Produto):
    def __init__(self, voltagem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voltagem = voltagem