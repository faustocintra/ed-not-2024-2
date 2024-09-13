comps = trocas = passd = 0           # Variáveis de estatística

def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô (na
    nossa implementação, será o último) e, na primeira
    passada, divide a lista, a partir da posição final do
    pivô, em uma sublista à esquerda, contendo apenas valores
    menores que o pivô, e outra sublista à direita, contendo
    apenas valores maiores que o pivô.
    Em seguida, recursivamente, repete o processo em cada uma
    das sublistas, até que toda a lista estaja ordenada.
    """
    global comps, trocas, passd

    # Quando não soubermos o valor da variável 'fim',
    # atribuímos a ela o valor da última posição da lista
    if fim is None: fim = len(lista) - 1

    passd += 1      # Inicia uma nova passada

    # Para que o algoritmo de ordenação possa ser aplicado,
    # é necessário que a faixa delimitada pelas variáveis
    # 'ini' e 'fim' tenha, pelo menos, dois elementos. Caso
    # contrário, saímos da função sem fazer nada
    if fim <= ini: return

    # Inicialização das variáveis
    pivot = fim
    div = ini - 1

    # Percorre a lista da posição 'ini' até a posição 'fim' - 1
    for pos in range(ini, fim):
        # Se o elemento da posição 'pos' for MENOR do que o
        # elemento da posição 'pivot', executa algumas ações
        
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1    # Avança 'div' em 1 posição
            # Efetua a troca entre os elementos das posições
            # 'pos' e 'div', caso sejam diferentes entre si
            if pos != div:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI
    # Após 'pos' chegar à sua posição final, 'div' deve ser
    # incrementado uma última vez
    div += 1

    # Troca os elementos das posições 'div' e 'pivot' entre si,
    # colocando este último em seu lugar definitivo, se ambos
    # forem diferentes entre si
    if div != pivot:
        lista[div], lista[pivot] = lista[pivot], lista[div]
        trocas += 1

    # Agora, todos os elementos à esquerda do pivô são MENORES
    # do que ele, enquanto todos os elementos à sua direita são
    # MAIORES do que ele. Chamamos a função recursivamente para
    # cada uma dessas sublistas
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

##################################################################

comps = trocas = passd = 0

#nums = [7, 9, 5, 4, 0, 3, 8, 1, 6, 2]

# Pior caso
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Melhor caso
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("ANTES:   ", nums)
quick_sort(nums)
print("DEPOIS:  ", nums)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")

##############################################################

from time import time

import sys, tracemalloc
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTES COM A LISTA DE NOMES
from data.nomes_desord import nomes

# Recortando os 100k primeiros nomes
# nomes = nomes[:100000]

comps = trocas = passd = 0

tracemalloc.start()     # Inicia medição do consumo de memória
hora_ini = time()
quick_sort(nomes)
hora_fim = time()

# Captura as informações do gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()      # Termina a medição da memória

print(nomes)
print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")