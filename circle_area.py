"""
Este arquivo utilizará o módulo math
para calcular a área de um círculo
"""
import math as m


def circle_area():
    """
    DocString da função, uma convenção do Python
    """
    radius = float(input('Raio do Círculo: '))
    radius_sqr = m.pow(radius, 2)
    calc_area = m.pi * (radius_sqr)
    return calc_area


area = circle_area()
print(area)
