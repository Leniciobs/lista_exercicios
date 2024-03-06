def menor_string(lista_strings):
    menor = lista_strings[0]
    for string in lista_strings:
        if len(string) < len(menor):
            menor = string
    return menor

lista = ["maçã", "banana", "laranja", "abacaxi", "uva"]
menor = menor_string(lista)
print("A menor string na lista é:", menor)
