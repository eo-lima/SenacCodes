class Estoque:
    lista_audio = []
    lista_eletroportatil = []
    lista_linhabranca = []
    lista_video = []

    @classmethod
    def todos_produtos(cls):
        return (
            cls.lista_audio
            + cls.lista_eletroportatil
            + cls.lista_linhabranca
            + cls.lista_video
        )

    @classmethod
    def buscar_produto(cls, nome):
        return next(
            (produto for produto in cls.todos_produtos() if produto._nome == nome),
            None,
        )
