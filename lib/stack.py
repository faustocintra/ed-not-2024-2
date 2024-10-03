class Stack:
    """
    ESTRUTURA DE DADOS PILHA
    É uma estrutura de dados linear de acesso restrito,
    na qual tanto a operação de inserção (tradicionalmente
    chamada de "push") quanto a operação de remoção ("pop")
    acontecem no final (ou topo). Em consequência, o
    funcionamento da pilha obedece ao princípio LIFO (Last
    In, First Out): o último elemento a entrar é o primeiro
    a sair.
    """
    def __init__(self):
        """ Método construtor """
        # Cria uma pilha privada e vazia para armazenar os
        # elementos da pilha
        self.__data = []

    def push(self, val):
        """
        Método para inserção
        Em pilhas, tem nome padronizado: push()
        """
        self.__data.append(val)     # Inserção sempre no final

    def is_empty(self):
        """
        Método que verifica se a pilha está ou não vazia
        """
        return len(self.__data) == 0
    
    def pop(self):
        """
        Método para remoção
        Em pilhas, tem nome padronizado: pop()
        """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma pilha vazia.")
        # Se chegou até aqui, a pilha NÃO está vazia e a
        # remoção pode ser feita
        return self.__data.pop()    # Remoção sempre no final
    
    def peek(self):
        """
        Método que permite consultar o valor que está no topo da
        pilha sem removê-lo
        Em pilhas, tem nome padronizado: peek()
        """
        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma pilha vazia.")
        return self.__data[-1]      # Último elemento da pilha
    
    def __str__(self):
        """ Método que permite exibir a pilha como string """
        return str(self.__data)
    
################################################################## 

# p = Stack()   # Cria uma nova pilha chamada p

# # Algumas inserções
# p.push(1001)
# p.push(1240)
# p.push(1131)
# p.push(1094)

# print(p)

# removido = p.pop()

# print("Removido:", removido)
# print(p)

# ultimo = p.peek()

# print("Último:", ultimo)
# print(p)