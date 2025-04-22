class Produto:
    def __init__(self, nome, tipo, descricao, composicao, quantidade, preco, permitido_para_menores):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.composicao = composicao
        self.quantidade = quantidade
        self.preco = preco
        self.permitido_para_menores = permitido_para_menores

    def __repr__(self):
        return f"{self.nome} ({self.tipo}): {self.preco} - {'Permitido' if self.permitido_para_menores else 'Não Permitido'}"