class Menu:
    def exibir_menu_principal(self):
        print("1. Entrar como Cliente")
        print("2. Entrar como Funcionário")
        escolha = input("Escolha uma opção: ")
        return escolha

    def exibir_menu_cliente(self):
        print("1. Visualizar Produtos")
        print("2. Adicionar ao Carrinho")
        print("3. Ver Carrinho")
        print("4. Pagar")
        escolha = input("Escolha uma opção: ")
        return escolha

    def exibir_menu_funcionario(self):
        print("1. Adicionar Produto")
        print("2. Alterar Produto")
        print("3. Remover Produto")
        escolha = input("Escolha uma opção: ")
        return escolha