# Importa a função formata_float_str_moeda do módulo helper dentro do pacote utils
from utils.helper import formata_float_str_moeda


# Define uma classe chamada Produto
class Produto:
    # Atributo de classe contador com valor inicial 1
    contador: int = 1

    # Define um método construtor que recebe um objeto, uma string nome e um float preco como parâmetros e retorna None
    def __init__(self: object, nome: str, preco: float) -> None:
        # Atribui o valor do contador ao atributo de instância privado __codigo
        self.__codigo: int = Produto.contador
        # Atribui o valor do parâmetro nome ao atributo de instância privado __nome
        self.__nome: str = nome
        # Atribui o valor do parâmetro preco ao atributo de instância privado __preco
        self.__preco: float = preco
        # Incrementa o valor do contador em 1
        Produto.contador += 1

    # Define um método getter para o atributo privado __codigo
    @property
    def codigo(self: object) -> int:
        return self.__codigo

    # Define um método getter para o atributo privado __nome
    @property
    def nome(self: object) -> str:
        return self.__nome

    # Define um método getter para o atributo privado __preco
    @property
    def preco(self: object) -> float:
        return self.__preco

    # Define um método especial __str__ que retorna uma string com a representação em string dos atributos da instância
    def __str__(self) -> str:
        # Utiliza a função formata_float_str_moeda para formatar o atributo __preco como moeda brasileira
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço {formata_float_str_moeda(self.preco)}'
