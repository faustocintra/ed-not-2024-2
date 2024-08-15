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

print("-" * 80)

# 4) ACESSANDO VALORES, INFORMANDO A RESPECTIVA POSIÇÃO
print("Elemento da QUINTA posição:", legumes[4])
print("Elemento da PRIMEIRA posição:", legumes[0])
print("Elemento da ÚLTIMA posição:", legumes[-1])
print("Elemento da PENÚLTIMA posição:", legumes[-2])

print("-" * 80)

# 5) SUBSTITUINDO VALORES EXISTENTES
print("ANTES:", legumes)

# Substituindo o valor na posição 3 (QUARTA posição)
legumes[3] = "vagem"
# Substituindo o valor na posição 0 (PRIMEIRA posição)
legumes[0] = "cará"
# Substituindo o valor na posição -1 (ÚLTIMA posição)
legumes[-1] = "inhame"

print("DEPOIS:", legumes)

print("-" * 80)

# 6) DETERMINANDO A QUANTIDADE DE ELEMENTOS DA LISTA: len()
print("Quantidade de elementos da lista de legumes:", len(legumes))
print("Quantidade de elementos da lista de números:", len(nums))

print("-" * 80)

# 7) REMOVENDO O *ÚLTIMO* ELEMENTO DE UMA LISTA: pop() (sem parâmetro)
print("ANTES:", legumes)
removido = legumes.pop()
print("Valor removido:", removido)
print("DEPOIS:", legumes)

print("-" * 80)

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() (com parâmetro)
removido = legumes.pop(3)
print("Elemento removido da posição 3:", removido)
print(legumes)

removido = legumes.pop(0)
print("Valor removido da primeira posição:", removido)
print(legumes)

print("-" * 80)

# 9) REMOVENDO UM ELEMENTO POR SEU VALOR: remove()
legumes.remove("mandioquinha")      # Não retorna valor
print(legumes)

print("-" * 80)

# 10) AUMENTANDO UMA LISTA COM ELEMENTOS DE OUTRA LISTA: extend()
mais_legumes = ["abobrinha", "quiabo", "jiló", "cabotiá", "chuchu"]
legumes.extend(mais_legumes)
print(legumes)

print("-" * 80)

# 11) FATIANDO UMA LISTA
#     Fatiar significa copiar um pedaço da lista (uma sublista),
#     criando uma nova lista

# Cria uma sublista que contém os elementos das posições 2 a 5
# (posição 6 *NÃO ENTRA*)
sublista2_5 = legumes[2:6]
print("Sublista de 2 a 5:", sublista2_5)

# Cria uma sublista que contém os elementos desde o início até
# a posição 6 (posição 7 *NÃO ENTRA*)
sublista_inicio_6 = legumes[:7]
print("Sublista do início à posição 6:", sublista_inicio_6)

# Cria uma sublista que contém os elementos da posição 4 até
# o final da lista
sublista4_fim = legumes[4:]
print("Sublista da posição 4 até o final:", sublista4_fim)