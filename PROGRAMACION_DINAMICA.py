def Grupo9_Mochila_ProgramacionDinamica(pesos, valores, capacidad):
    n = len(pesos)

    DP = [[0] * (capacidad + 1) for _ in range(n)]

    for w in range(1, capacidad + 1):
        if pesos[0] <= w:
            DP[0][w] = valores[0]
        else:
            DP[0][w] = 0

    for i in range(1, n):
        peso_i = pesos[i]
        valor_i = valores[i]

        for w in range(1, capacidad + 1):

            if peso_i > w:
                DP[i][w] = DP[i - 1][w]
            else:
                valor_sin = DP[i - 1][w]
                capacidad_restante = w - peso_i

                if capacidad_restante <= 0:
                    valor_con = valor_i
                else:
                    valor_con = valor_i + DP[i - 1][capacidad_restante]

                DP[i][w] = max(valor_sin, valor_con)

    return DP[n - 1][capacidad]


if __name__ == "__main__":
    n = int(input("Número de objetos: "))
    pesos = []
    valores = []

    for i in range(1, n + 1):
        peso = int(input(f"Peso del objeto {i}: "))
        valor = int(input(f"Valor del objeto {i}: "))
        pesos.append(peso)
        valores.append(valor)

    capacidad = int(input("Capacidad de la mochila: "))

    resultado = Grupo9_Mochila_ProgramacionDinamica(pesos, valores, capacidad)
    print("Mejor valor encontrado con Programación Dinámica:", resultado)
