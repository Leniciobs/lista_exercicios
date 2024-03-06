def intersecao(lista1, lista2):
    intersecao_lista = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in intersecao_lista:
            intersecao_lista.append(elemento)
    return intersecao_lista

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
print("A interseção das listas é:", intersecao(lista1, lista2))
