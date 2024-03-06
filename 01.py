def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

texto = input("Digite uma string: ")
print("O número de vogais na string é:", contar_vogais(texto))
