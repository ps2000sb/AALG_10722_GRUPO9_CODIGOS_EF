def Grupo9_Mochila_FuerzaBruta(pesos, valores, capacidad):
    n = len(pesos)
    mejor_valor = 0
    max_subconjuntos = 2 ** n

    for mask in range(max_subconjuntos):
        peso_actual = 0
        valor_actual = 0
        temp_mask = mask

        for j in range(n):
            bit = temp_mask % 2
            if bit == 1:
                peso_actual += pesos[j]
                valor_actual += valores[j]
            temp_mask //= 2

        if peso_actual <= capacidad and valor_actual > mejor_valor:
            mejor_valor = valor_actual

    return mejor_valor


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

    resultado = Grupo9_Mochila_FuerzaBruta(pesos, valores, capacidad)
    print("Mejor valor encontrado con Fuerza Bruta:", resultado)
