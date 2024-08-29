def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas, 
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última passada,
    nenhuma troca tenha sido efetuada.
    """

    # Loop eterno: não sabemos antecipadamente quantas passadas
    # serão necessárias
    while True:

        # Variável que controla se houve troca na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        for pos in range(len(lista) - 1):
            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # efetuamos uma TROCA entre eles
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True       # Houve troca na passada

        # <~ CUIDADO COM A INDENTAÇÃO AQUI
        # Se não houve troca na passada (trocou é False), a lista
        # está ordenada e interrompemos o loop eterno while
        if not trocou:
            break

######################################################################

nums = [7, 9, 5, 4, 0, 3, 8, 1, 6, 2]

print("ANTES: ", nums)
bubble_sort(nums)
print("DEPOIS:", nums)