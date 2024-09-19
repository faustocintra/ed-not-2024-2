"""
Classe é uma estrutura que representa conjuntamente dados e
algoritmos. Uma classe pode ser comparado a uma "assadeira",
com a qual se pode produzir diferentes tipos de "assados",
variando os "ingredientes" (dados) da receita e o "modo de
fazer" (algoritmos). Apesar dessas variações, todos os objetos
criados a partir de uma mesma classe terão sempre algumas
características comuns, impostas por ela.
"""
from math import pi

class FormaGeometrica:
    """
    Por convenção, nomes de classe seguem o formato PascalCase
    (primeira letra de cada palavra em maiúsculo).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, representando os algoritmos). Uma função especial,
    chamada __init__, é chamada sempre que se tenta criar um
    novo objeto a partir de uma classe. Essa função especial é
    chamada de CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS; seu primeiro parâmetro
       é sempre self, representando o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """