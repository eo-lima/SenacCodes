from pessoas import Pessoa

class Vendedor(Pessoa):
    def __init__(self, email, *args, **kwargs):
        super().__init__()
        self.email = email