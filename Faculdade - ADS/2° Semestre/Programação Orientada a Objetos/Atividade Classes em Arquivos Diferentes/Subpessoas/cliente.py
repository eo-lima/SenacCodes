from pessoas import Pessoa

class Cliente(Pessoa):

    compras = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        