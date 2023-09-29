class Fornecedor:
    def __init__(self, cnpj, nome):
        self.cnpj = cnpj
        self.nome = nome


class Produto:
    def __init__(self, codigo, descricao, preco_compra, preco_venda, quantidade, estoque_minimo, fornecedor):
        self.codigo = codigo
        self.descricao = descricao
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo
        self.fornecedor = fornecedor

    def compra(self, quant, valor):
        self.quantidade += quant
        self.preco_compra = (self.preco_compra * (self.quantidade - quant) + valor) / self.quantidade

    def venda(self, quant):
        if quant <= self.quantidade:
            self.quantidade -= quant
            return quant * self.preco_venda
        else:
            print("Quantidade insuficiente em estoque.")
            return 0

# Exemplo de uso:
fornecedor = Fornecedor("12345678900001", "Fornecedor ABC")
produto = Produto("001", "Produto A", 5.0, 10.0, 50, 10, fornecedor)

# Realizando uma compra de 20 unidades por R$ 7,50 cada
produto.compra(20, 150.0)

# Realizando uma venda de 15 unidades
valor_venda = produto.venda(15)
print(f"Valor da venda: R${valor_venda:.2f}")

# Exibindo informações do produto após as transações
print(f"Descrição: {produto.descricao}")
print(f"Quantidade em estoque: {produto.quantidade}")
print(f"Preço de compra: R${produto.preco_compra:.2f}")
print(f"Preço de venda: R${produto.preco_venda:.2f}")
