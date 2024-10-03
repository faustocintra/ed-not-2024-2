""" 
Programa simples que inverte uma palavra informada pelo usuário
e verifica se ela é um PALÍNDROMO, isto é, uma palavra que pode
ser lida tanto da frente para trás quanto de trás para frente.

Esta implementação usa a classe Stack para gerar uma pilha.
"""
from lib.stack import Stack

palavra = input("Informe a palavra a ser verificada: ")

# Cria uma nova pilha a partir da classe Stack
pilha = Stack()

# PARTE 1: PREENCHIMENTO DA PILHA
# Pega cada letra da palavra (convertida em maiúsculas, para
# facilitar a posterior comparação) e insere no final (topo)
# da pilha
for letra in palavra.upper():
    pilha.push(letra)
    print(pilha)

print("-" * 80)

# PARTE 2: ESVAZIAMENTO DA PILHA
# Enquanto a pilha não estiver vazia, vamos retirando a última
# letra dela e concatenando-a à variável inverso
inverso = ""
while not pilha.is_empty():
    letra = pilha.pop()
    inverso += letra
    print(f"PILHA: {pilha}, inverso: {inverso}")

if palavra.upper() == inverso:
    print(f"*** A palavra {inverso} é um PALÍNDROMO ***")
else:
    print(f"--- A palavra {palavra.upper()} NÃO É um palíndromo ---")