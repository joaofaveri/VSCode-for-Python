"""
Seção sobre formatação de código
Formatadores fornecem um estilo consistente para formatação
"""
number = [2, 4, 6, 8]

for each_num in number:
    # pylint: disable=C0103
    # Desabilita a verificação da variável pelo pylint
    # Ao usar o nome 'num', confundiu a variável com uma constante
    each_num = each_num * 2
    print(each_num)
