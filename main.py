from Produto import Produto
from Categoria import Categoria

adicionaProduto = input('Insira o nome do produto que deseja adicionar: ')
adicionaCod = input('Insira o código do produto que deseja adicionar: ')
adicionaPreco = float(input('Insira o preço do produto que deseja adicionar: '))
adicionarQnt = int(input('Insira a quantidade de produto para adicionar: '))


produto = Produto(adicionaCod, adicionaProduto, adicionaPreco, adicionarQnt)

adicionaCategoria = input(f'Insira a categoria que o produto {adicionaProduto} se encaixa: ')

produto.setCategoria(adicionaCategoria)

produto.cadastrar()