# La funciones recursivas son aquella que internamente se invocan a si misma
# Las funciones recursivas siempre deben tener una condicion de cierre
# Las funciones recursivas son siempre ciclicas

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(999)

print(f"El factorial de 20 es: {resultado}")


