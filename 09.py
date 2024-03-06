def encontrar_par_soma(lista, soma_desejada):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == soma_desejada:
                pares.append((lista[i], lista[j]))
    return pares

lista = [1, 2, 3, 4, 5, 6, 7]
soma_desejada = 8
pares_encontrados = encontrar_par_soma(lista, soma_desejada)
print("Pares cuja soma é", soma_desejada, ":", pares_encontrados)
