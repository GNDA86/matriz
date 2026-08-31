matriz = [[1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]

print("=== INGRESO DE 25 VALORES A LA MATRIZ 5x5 ===")

for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\n=== MATRIZ 5x5 RESULTANTE ===")
for i in range(5):
    for j in range(5):
        print(f"{matriz[i][j]:4d}", end=" ")
    print()
    