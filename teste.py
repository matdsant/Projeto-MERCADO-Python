# Importa a classe Produto do módulo produto dentro do pacote models
from models.produto import Produto

# Cria uma instância da classe Produto com o nome 'Playstation 4' e o preço '1797,33' e atribui à variável ps4
ps4 = Produto('Playstation 4', 1797.33)

# Cria uma instância da classe Produto com o nome 'Xbox ONE X' e o preço '1643,99' e atribui à variável xbox
xbox = Produto('Xbox ONE X', 1643.99)

# Imprime a representação em string do objeto ps4 na saída padrão
print(ps4)

# Imprime a representação em string do objeto xbox na saída padrão
print(xbox)
