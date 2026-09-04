from produtos import Produto

class Audio(Produto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)