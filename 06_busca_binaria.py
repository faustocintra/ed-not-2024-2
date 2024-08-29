comps = None        # Contador de comparações

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor
    de busca, divide a lista em duas partes, procurando pelo valor
    de busca apenas na parte onde o valor de busca poderia estar.
    Novas subdivisões são feitas até que se encontre o valor de
    busca ou que reste apenas uma sublista vazia, quando então se
    conclui que o valor de busca não existe na lista.
    """

    # Avisa à função para usar a variável comps declarada
    # fora dela, no escopo global
    global comps
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        # Calculando o meio da lista
        meio = (ini + fim) // 2     # Divisão inteira

        # Verifica se o valor que está no meio da lista é
        # igual ao valor de busca. Em caso afirmativo, 
        # retornamos a posição do meio, pois o valor de
        # busca foi encontrado
        if val == lista[meio]:
            comps += 1
            return meio
        
        # Senão, se o valor de busca é MENOR do que o valor
        # do meio, move o ponteiro do fim para a posição
        # anterior à do meio e reinicia a busca na metade
        # ESQUERDA da (sub)lista
        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        # Por fim, se o valor de busca é MAIOR do que o valor
        # do meio da lista, move o ponteiro de início para a
        # posição seguinte à do meio e reinicia a busca na
        # metade DIREITA da (sub)lista
        else:
            comps += 2
            ini = meio + 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI
    # Se chegamos a esse ponto, é porque o valor de busca não
    # existe na lista
    return -1

##############################################################

from time import time

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

# TESTES COM A LISTA DE NOMES
from data.nomes_completos import nomes

hora_ini = time()
resultado1 = busca_binaria(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {resultado1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Número de comparações: {comps}\n\n")

hora_ini = time()
resultado2 = busca_binaria(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERREIRA encontrada na posição {resultado2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Número de comparações: {comps}\n\n")

hora_ini = time()
resultado3 = busca_binaria(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição {resultado3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Número de comparações: {comps}\n\n")

hora_ini = time()
resultado4 = busca_binaria(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontrada na posição {resultado4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Número de comparações: {comps}\n\n")