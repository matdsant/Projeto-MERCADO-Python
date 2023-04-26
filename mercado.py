# Importa as classes List e Dict do módulo typing, e a função sleep do módulo time, e a classe Produto do módulo
# models.produto e a função formata_float_str_moeda do módulo utils.helper
from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda

# Cria uma lista vazia de produtos e uma lista vazia de dicionários com chave Produto e valor inteiro
produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


# Define a função main, que chama a função menu
def main() -> None:
    menu()


# Define a função menu, que mostra o menu de opções e chama a função correspondente à opção escolhida pelo usuário
def menu() -> None:
    print('=========================================')
    print('============ Bem-Vindo(a) ===============')
    print('============ Tomate  Shop ===============')
    print('=========================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produtos')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Obrigado pela preferência!')
        print('      Volte sempre!       ')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        menu()


# Define a função cadastrar_produto, que solicita ao usuário o nome e o preço do produto, cria um objeto Produto com
# esses dados e o adiciona à lista produtos
def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


# Define a função listar_produtos, que mostra na tela a lista de produtos cadastrados, ou uma mensagem indicando que
# ainda não há produtos cadastrados
def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('====================')
        for produto in produtos:
            print(produto)
            print('-----')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(1)
    menu()


# Define a função comprar_produto, que mostra na tela a lista de produtos disponíveis e solicita ao usuário o código
# do produto que deseja comprar, e a quantidade. Em seguida, adiciona o produto e a quantidade ao carrinho
def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que você deseja adicionar ao carrinho: ')
        print('===================================================================')
        for produto in produtos:
            print(produto)
            print('--------------------------------')
            sleep(1)
        codigo: int = int(input())
        quantidade: int = int(input('Informe a quantidade que deseja adicionar ao carrinho: '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + quantidade
                        print(f'O produto {produto.nome} agora possui {quant + quantidade} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: quantidade}
                    carrinho.append(prod)
                    print(f'{quantidade} unidades do produto {produto.nome} foram adicionadas ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: quantidade}
                carrinho.append(item)
                print(f'{quantidade} unidades do produto {produto.nome} foram adicionadas ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
        sleep(2)
        menu()


# Define a função visualizar_carrinho, que mostra na tela os produtos e suas quantidades presentes no carrinho,
# ou uma mensagem indicando que o carrinho está vazio
def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        print('======================')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('=======================')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


# Define a função fechar_pedido, que mostra na tela os produtos presentes no carrinho, seu valor total e limpa o
# carrinho
def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no Carrinho')
        print('====================')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('===================')
                sleep(1)
        print(f'A sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


# Define a função pega_produto_por_codigo, que recebe um código de produto e retorna o objeto Produto correspondente,
# se existir na lista de produtos
def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


# Chama a função main quando o módulo é executado diretamente
if __name__ == '__main__':
    main()
