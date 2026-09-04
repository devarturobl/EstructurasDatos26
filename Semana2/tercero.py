def encontrar(nums, target):
    coleccion = set()
    tamaño = len(nums)
    for num in nums:
        resta = target - num
        if resta in coleccion:
            return f"Encontre a: ({num}, {resta})"
        coleccion.add(num)
    return "Par no encontrado"

nums1 = [8, 7, 2, 5, 3, 1, 10, 5, 4, 6]
target1 = 5
print(encontrar(nums1, target1))  # Salida: Par encontrado