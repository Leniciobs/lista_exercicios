def contar_ocorrencias(frase, palavra):
    palavras_na_frase = frase.split()
    contador = 0
    for p in palavras_na_frase:
        if p == palavra:
            contador += 1
    return contador

frase = input("Digite uma frase: ")
palavra_busca = input("Digite a palavra que deseja contar: ")
print("O número de ocorrências da palavra na frase é:", contar_ocorrencias(frase, palavra_busca))
