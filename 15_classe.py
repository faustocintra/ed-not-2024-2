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

    def __init__(self, base, altura, tipo):
        """ Método construtor """

        # Valida se base é numérica e maior que zero
        if type(base) not in [int, float] or base <= 0:
            raise Exception("ERRO: 'base' deve ser numérica e maior que zero.")
        
        # Valida se altura é numérica e maior que zero
        if type(altura) not in [int, float] or altura <= 0:
            raise Exception("ERRO: 'altura' deve ser numérica e maior que zero")
        
        # Valida o tipo de forma
        if tipo not in ["R", "T", "E"]:
            raise Exception("ERRO: 'tipo' deve ser 'R', 'T' ou 'E'.")
        
        # Se chegamos até aqui, os valores passados são válidos
        # e podemos armazená-los como atributos do objeto que
        # está sendo criado
        self.__base = base
        self.__altura = altura
        self.__tipo = tipo

    def set_base(self, val):
        """ Método setter para o atributo __base """
        # Valida se base é numérica e maior que zero
        if type(val) not in [int, float] or val <= 0:
            raise Exception("ERRO: 'base' deve ser numérica e maior que zero.")
        # Sobreviveu à validação, armazena val no atributo
        self.__base = val

    def set_altura(self, val):
        """ Método setter para o atributo __altura """
        # Valida se altura é numérica e maior que zero
        if type(val) not in [int, float] or val <= 0:
            raise Exception("ERRO: 'altura' deve ser numérica e maior que zero")
        # Sobreviveu à validação, armazena val no atributo
        self.__altura = val

    def set_tipo(self, val):
        """ Método setter para o atributo __tipo """
        # Valida o tipo de forma
        if val not in ["R", "T", "E"]:
            raise Exception("ERRO: 'tipo' deve ser 'R', 'T' ou 'E'.")
        # Sobreviveu à validação, armazena val no atributo
        self.__tipo = val



###########################################################################

# Criando uma forma geométrica a partir da classe
forma1 = FormaGeometrica(20, 12.5, "R")

# Nesse ponto, o objeto já existe, podemos modificar seus atributos
forma1.base = "tomate"
forma1.altura = -7
forma1.tipo = "W"

print(f"Dados da forma1: base = {forma1.base}, altura = {forma1.altura}, tipo = {forma1.tipo}")