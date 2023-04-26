# Define uma função chamada formata_float_str_moeda que recebe um valor do tipo float e retorna uma string formatada
# como moeda brasileira
def formata_float_str_moeda(valor: float) -> str:
    # Utiliza a sintaxe de f-string para formatar o valor como moeda brasileira, com R$ no início, vírgula como
    # separador de milhar e duas casas decimais
    return f'R$ {valor:,.2f}'
