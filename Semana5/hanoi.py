def hanoi(n, origen, destino, auxiliar):
    # Caso base: si solo queda un disco
    if n == 1:
        print(f"Mover disco 1 de {origen} <a> {destino}")
        return
    
    # Paso A: Mover los n-1 discos superiores del origen al auxiliar
    hanoi(n - 1, origen, auxiliar, destino)
    
    # Paso B: Mover el disco más grande del origen al destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Paso C: Mover los n-1 discos del auxiliar al destino usando el origen como apoyo
    hanoi(n - 1, auxiliar, destino, origen)

hanoi(4,"A","C","B")