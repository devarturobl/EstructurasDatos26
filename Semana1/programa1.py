from collections import deque

milista = [9,10,70]

milista.append(8)
milista.append(4)
milista.append(9)
milista.append(81)
milista.append(456)

tamaño = len(milista)

print(f"esta es mi lista: {milista}")
print(f"el tamaño de mi lista es de: {tamaño}")

# como cola
cola = deque()
