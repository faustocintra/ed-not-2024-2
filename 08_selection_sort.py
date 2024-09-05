comps = trocas = passd = None

def selection_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e, em seguida,
    encontra o menor valor entre os elementos do restante da lista.
    Se o valor encontrado for MENOR que o valor previamente
    selecionado, efetua a troca entre eles. Continuando, seleciona
    o segundo elemento da lista, buscando pelo menor valor nas
    posições subsequentes. Faz a troca entre os dois valores, se
    necessário. O processo se repete até que o penúltimo elemento
    da lista seja selecionado, comparado com o último e feita a
    troca entre eles, se for o caso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop que vai da primeira até a PENÚLTIMA posição para
    # selecionar o elemento que será comparado aos demais
    for pos_sel in range(len(lista) - 1):

        passd += 1      # Inicia uma nova passada

        # Inicia supondo que a posição do menor valor do resto
        # da lista é o que está imediatamente à frente do valor
        # selecionado
        pos_menor = pos_sel + 1

        # Percorre o restante da lista, da posição seguinte a
        # pos_menor até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor que estiver na posição (pos) atual for
            # MENOR que aquele apontado por pos_menor, ajusta 
            # pos_menor para o mesmo valor de pos

            comps += 1      # Comparação do if abaixo
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # <~ CUIDADO COM A INDENTAÇÃO!
        # Neste ponto, já terminamos de percorrer o restante da
        # lista e sabemos a posição do menor valor que há nele.
        # Comparamos, então, os valores das posições pos_menor e
        # pos_sel. Se o primeiro for MENOR que o segundo, fazemos
        # a troca entre eles

        comps += 1      # Comparação do if abaixo
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

##################################################################

# nums = [7, 9, 5, 4, 0, 3, 8, 1, 6, 2]

# Pior caso
nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# Melhor caso
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("ANTES: ", nums)
selection_sort(nums)
print("DEPOIS:", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")

##############################################################

from time import time

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTES COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Recortando os 100k primeiros nomes
nomes = nomes[:100000]

hora_ini = time()
selection_sort(nomes)
hora_fim = time()

print(nomes)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")