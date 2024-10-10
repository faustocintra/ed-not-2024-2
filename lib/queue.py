class Queue:
    """
    ESTRUTURA DE DADOS FILA
    Trata-se de uma estrutura de dados linear em que a operação
    de inserção ("enqueue") ocorre no final (ou cauda) da
    estrutura, enquanto a operação de remoção ("dequeue") é
    feita no início (cabeça). Em consequência, o funcionamento
    da fila pode ser descrito pelo princípio FIFO (First In,
    First Out): o primeiro a entrar também é o primeiro a sair.
    """
    def __init__(self):
        """ Método construtor """
        self.__data = []    # Lista vazia

    def enqueue(self, val):
        """
        Método de inserção
        Em filas, tem nome padronizado: enqueue
        """
        self.__data.append(val)     # Inserção no final

    def is_empty(self):
        """ Método que retorna se a fila está ou não vazia """
        return len(self.__data) == 0
    
    def dequeue(self):
        """
        Método de remoção
        Em filas, tem nome padronizado: dequeue
        """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma fila vazia.")
        return self.__data.pop(0)   # Remoção no início
    
    def peek(self):
        """ 
        Método para consultar o primeiro item da fila, 
        sem removê-lo
        """
        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma fila vazia.")
        return self.__data[0]       # Primeiro item
    
    def __str__(self):
        """ Método que retorna uma representação da fila como string """
        return str(self.__data)

###################################################################