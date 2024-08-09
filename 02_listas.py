"""
LISTA é uma estrutura de dados nativa da linguagem
Python. Ela permite que vários valores sejam associados
a uma única variável
"""

# Lista de strings
legumes = ["batata", "cenoura", "beterraba", "mandioca", "nabo"]

# Lista de números
nums = [3, 10, -7, 12.8, -0.5, 4, 22]

# Lista com valores de vários tipos (pouco comum)
mistureba = ["Joaquim", 37, 1.81, 79, True]

##### OPERAÇÕES SOBRE LISTAS #####

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um de seus itens e
# fazer algo com ele. No exemplo a seguir, vamos dar print() em
# cada um dos legumes da lista
for x in legumes:
    print(x)

# Traço separador
print("-" * 80)

# Percorrendo a lista de números e exibindo o valor do dobro de 
# cada item
for n in nums:
    print(n * 2)

print("-" * 80)

#2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()
print('legumes, antes:', legumes)
print('nums, antes:', nums)

# Inserindo novos itens ao final das listas
legumes.append("batata-doce")
nums.append(-11)

print('legumes, depois:', legumes)
print('nums, depois:', nums)

print("-" * 80)

# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º ~> a posição onde será feita a inserção (A CONTAGEM COMEÇA
#          EM ZERO)
#    2º ~> o novo elemento a ser inserido

# Inserindo um novo elemento na QUARTA posição
legumes.insert(3, "mandioquinha")
print(legumes)

# Inserindo um novo elemento na PRIMEIRA posição
legumes.insert(0, "cebola")
print(legumes)