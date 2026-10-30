from config.conexao import conectar
class Produto:
    def __init__(self, id_produto, nome, preco, quantidade, garantia):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.garantia = garantia

    def inserir(self, produto):
        conn = conectar()
        try:
            cur = conn.cursor()
            cur.execute(" INSERT INTO produto (nome, preco, quantidade, garantia) VALUES (%s,%s,%s,%s)", (produto.nome, produto.preco, produto.quantidade, produto.garantia))
            conn.commit()
            produto.id_produto = cur.lastrowid

            return produto
        finally:
            conn.close
            
