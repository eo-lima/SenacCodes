from pessoas import Pessoa

class Cliente(Pessoa):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fazer_pedido(self):
        pass