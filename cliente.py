from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, data_nascimento, endereco):
        super().__init__(nome)
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.carrinho = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        self.carrinho.append((produto, quantidade))

    def visualizar_carrinho(self):
        return [(p.nome, q, p.preco * q) for p, q in self.carrinho]

    def calcular_total(self):
        return sum(p.preco * q for p, q in self.carrinho)