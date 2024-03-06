def contar_palavras(string):
    palavras = string.split()
    return len(palavras)

texto = input("Digite uma string: ")
print("O número de palavras na string é:", contar_palavras(texto))
