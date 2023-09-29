''' Aqui está a implementação da classe Estoque que gerencia produtos,
 incluindo as operações de compra e venda:  '''

class Produto:
    def __init__(self, codigo, descricao, preco_compra, preco_venda, estoque_minimo):
        self.codigo = codigo
        self.descricao = descricao
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.estoque_minimo = estoque_minimo
        self.quantidade = 0  # Inicializa a quantidade como zero

    def compra(self, quant, valor):
        self.quantidade += quant
        self.preco_compra = valor / quant

    def venda(self, quant):
        if quant <= self.quantidade:
            self.quantidade -= quant
            return quant * self.preco_venda
        else:
            print("Quantidade insuficiente em estoque.")
            return 0


class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, codigo, descricao, preco_compra, preco_venda, estoque_minimo):
        produto = Produto(codigo, descricao, preco_compra, preco_venda, estoque_minimo)
        self.produtos[codigo] = produto

    def comprar(self, codigo, quant, valor):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            produto.compra(quant, valor)
        else:
            print("Produto não encontrado.")

    def vender(self, codigo, quant):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            valor_total = produto.venda(quant)
            if valor_total > 0:
                print(f"Venda realizada. Valor total: R${valor_total:.2f}")
            else:
                print("Venda não realizada.")
        else:
            print("Produto não encontrado.")


# Exemplo de uso:
estoque = Estoque()

# Cadastrando produtos no estoque
estoque.cadastrar_produto("001", "Produto A", 5.0, 10.0, 10)
estoque.cadastrar_produto("002", "Produto B", 3.0, 8.0, 5)

# Comprando produtos
estoque.comprar("001", 20, 150.0)
estoque.comprar("002", 15, 50.0)

# Vendendo produtos
estoque.vender("001", 10)
estoque.vender("002", 8)

# Exibindo informações do estoque
for codigo, produto in estoque.produtos.items():
    print(f"Produto {codigo}: {produto.descricao}")
    print(f"Quantidade em estoque: {produto.quantidade}")
    print(f"Preço de compra: R${produto.preco_compra:.2f}")
    print(f"Preço de venda: R${produto.preco_venda:.2f}")
    print("---")

'''
Foi criada uma classe Produto que é utilizada na classe Estoque. 
A classe Estoque possui métodos para cadastrar produtos, realizar compras e vendas. 
O exemplo de mostra como criar um estoque, cadastrar produtos, realizar compras e vendas,
e exibir informações do estoque.'''