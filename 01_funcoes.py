"""
Função que calcula o Índice de Massa Corporal (IMC)
de uma pessoa, dados seu peso e sua altura
"""
def imc(peso, altura):
    resultado = peso / altura ** 2
    return resultado

print("O IMC de uma pessoa com 1,74m e 81kg é ", imc(81, 1.74))

####################################################################

from math import pi

"""
Função que calcula a área de uma forma geométrica plana, dadas
as medidas da base e da altura e o tipo de forma
"""
def calc_area(base, altura, tipo):
    if tipo == "R":         # Retângulo
        return base * altura
    elif tipo == "T":       # Triângulo
        return base * altura / 2
    elif tipo == "E":       # Elipse
        return (base / 2) * (altura / 2) * pi
    else:                   # Tipo de forma inválido
        return None
    
print(f"Área retângulo 22x47: {calc_area(22, 47, 'R')}")
print(f"Área triângulo 12,5x25: {calc_area(12.5, 25, 'T')}")
print(f"Área elipse 20x30: {calc_area(20, 30, 'E')}")
print(f"Área inválida 8x11,5: {calc_area(8, 11.5, 'W')}")