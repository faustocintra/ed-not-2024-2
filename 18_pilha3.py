"""
Programa simples que verifica o balanceamento de parênteses
em expressões matemáticas usando pilha
"""
from lib.stack import Stack

pilha = Stack()

# expr = "(2 * (3 + 4) - (5 / 3) + 1) - 2"
# expr = "(2 * ((3 + 4) - ((5 / 3) + 1) - 2"
expr = "(2 * (3 + 4)) - (5 / 3) + 1)) - 2"


for pos in range(len(expr)):
    # 1ª PARTE: percorre a expressão e EMPILHA as posições onde
    # são encontrados os caracteres de abre parêntese
    if expr[pos] == "(": pilha.push(pos)

    # 2ª PARTE: ao encontrar um caractere de fecha parêntese,
    # tenta desempilhar
    elif expr[pos] == ")":
        # A pilha não pode estar vazia quando for encontrado um
        # fecha parêntese
        if pilha.is_empty():
            print(f"ERRO: parêntese fechado na posição {pos} não tem o abre correspondente.")
        else:
            pos_emp = pilha.pop()
            print(f"Parêntese aberto na posição {pos_emp} foi fechado na posição {pos}.")

print(pilha)

# <~ CUIDADO COM A INDENTAÇÃO AQUI!
# Processa eventuais sobras na pilha após o término da 
# análise da expressão
while not pilha.is_empty():
    pos_emp = pilha.pop()
    print(f"ERRO: parêntese aberto na posição {pos_emp} não tem o fecha correspondente")