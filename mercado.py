from cliente import Cliente
from funcionario import Funcionario
from estoque import Estoque
from menu import Menu

class Mercado:
    def __init__(self, arquivo_estoque):
        self.estoque = Estoque(arquivo_estoque)
        self.menu = Menu()

    def iniciar(self):
        while True:
            escolha = self.menu.exibir_menu_principal()
            if escolha == '1':
                self.entrar_como_cliente()
            elif escolha == '2':
                self.entrar_como_funcionario()
            else:
                print("Opção inválida!")

    def entrar_como_cliente(self):
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereço: ")
        cliente = Cliente(nome, data_nascimento, endereco)
        while True:
            escolha = self.menu.exibir_menu_cliente()
            if escolha == '1':
                self.visualizar_produtos()
            elif escolha == '2':
                pass # Implementar adicionar ao carrinho
            elif escolha == '3':
                pass # Implementar visualizar carrinho
            elif escolha == '4':
                pass # Implementar pagamento
            else:
                print("Opção inválida!")

    def entrar_como_funcionario(self):
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        # Autenticar funcionário (omitir autenticação por simplicidade)
        while True:
            escolha = self.menu.exibir_menu_funcionario()
            if escolha == '1':
                pass # Implementar adicionar produto
            elif escolha == '2':
                pass # Implementar alterar produto
            elif escolha == '3':
                pass # Implementar remover produto
            else:
                print("Opção inválida!")

    def visualizar_produtos(self):
        produtos = self.estoque.produtos
        for produto in produtos:
            print(produto)