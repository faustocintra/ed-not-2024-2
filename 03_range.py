"""
range() é uma função da linguagem Python que gera uma faixa
de números. É muito usada em associação com listas e com a
instrução for.
"""

# 1) range() com *UM* parâmetro
#    Gera uma faixa numérica que vai de 0 (zero) até o
#    valor do parâmetro - 1
for num in range(10):
    print(num)

print("-" * 80)

# 2) range() com *DOIS* parâmetros
#    1º parâmetro ~> valor inicial da faixa
#    2º parâmetro ~> valor final da faixa (*NÃO INCLUÍDO*)
for x in range(10, 16):
    print(x) 

print("-" * 80)

# 3) range() com *TRÊS* parâmetros
#    1º parâmetro ~> valor inicial
#    2º parâmetro ~> valor final (*NÃO INCLUÍDO*)
#    3º parâmetro ~> valor do passo (intervalo entre um número e o próximo)
for n in range(0, 22, 3):   # De 0 a 21 contando de 3 em 3
    print(n)

print("-" * 80)

# range() com passo negativo
for i in range(10, 0, -1):
    print(i)