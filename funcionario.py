from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, usuario, senha):
        super().__init__(nome)
        self.usuario = usuario
        self.senha = senha