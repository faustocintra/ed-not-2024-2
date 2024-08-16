frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibir apenas seus elementos, usamos
# a estrutura for..in, como já visto no arquivo nº 02
for f in frutas:
    print(f)

print("-" * 80)

# Percorrendo uma lista em ordem reversa: reversed()
for x in reversed(frutas):
    print(x)

print("-" * 80)

# No entanto, frequentemente, precisamos exibir, além do valor do
# elemento, também sua posição. Nesse caso, devemos usar a função
# for..in combinada com as funções range() e len()
for pos in range(len(frutas)):
    print(f"Posição {pos} => {frutas[pos]}")

print("-" * 80)

# Às vezes, é necessário percorrer a lista de trás para a frente,
# mas tendo acesso também às posições dos elementos. Assim, usamos
# a estrutura for..in, len() e range() com três parâmetros
for i in range(len(frutas) - 1, -1, -1):
    print(f"Posição {i} => {frutas[i]}")
