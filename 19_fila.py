from lib.queue import Queue

# Inicializa uma fila
fila_ubs = Queue()

# Insere algumas pessoas na fila
fila_ubs.enqueue("Leonilda")
fila_ubs.enqueue("Otacílio")
fila_ubs.enqueue("Waldisney")
fila_ubs.enqueue("Adamastor")

print(fila_ubs)

# Atende uma pessoa
atendido = fila_ubs.dequeue()
print(f"Foi atendido: {atendido}")
print(fila_ubs)

# Consulta quem será o próximo a ser atendido
proximo = fila_ubs.peek()
print(f"{proximo} será o próximo a ser atendido")
print(fila_ubs)

# Mais duas pessoas chegaram na fila
fila_ubs.enqueue("Margarete")
fila_ubs.enqueue("Gervásio")
print(fila_ubs)

# Atende o primeiro da fila
atendido = fila_ubs.dequeue()
print(f"Foi atendido: {atendido}")
print(fila_ubs)