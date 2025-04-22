import json
from produto import Produto 

class Estoque:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        with open(self.arquivo, 'r') as f:
            dados = json.load(f)
            return [Produto(**p) for p in dados['produtos']]

    def salvar_produtos(self):
        dados = {'produtos': [vars(p) for p in self.produtos]}
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.salvar_produtos()

    def remover_produto(self, nome):
        self.produtos = [p for p in self.produtos if p.nome != nome]
        self.salvar_produtos()

    def atualizar_produto(self, nome, **kwargs):
        for produto in self.produtos:
            if produto.nome == nome:
                for chave, valor in kwargs.items():
                    setattr(produto, chave, valor)
                self.salvar_produtos()
                break