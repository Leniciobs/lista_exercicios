def k_maiores(lista, k):
    lista_ordenada = sorted(lista, reverse=True)
    maiores = lista_ordenada[:k]
    maiores_ordem_original = [x for x in lista if x in maiores]
    return maiores_ordem_original

lista = [4, 2, 7, 1, 9, 5, 3, 8, 6]
k = int(input("Digite o valor de k: "))
print("Os", k, "maiores elementos na lista são:", k_maiores(lista, k))
