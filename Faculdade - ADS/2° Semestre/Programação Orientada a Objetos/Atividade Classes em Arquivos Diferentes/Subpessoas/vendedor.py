from pessoas import Pessoa

class Vendedor(Pessoa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._comissao = 0