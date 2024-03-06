def calcular_frequencia(texto, palavra):
    texto = texto.lower()
    palavra = palavra.lower()
    palavras = texto.split()
    ocorrencias = palavras.count(palavra)
    frequencia = ocorrencias / len(palavras)
    return frequencia

texto = "Este é um exemplo de texto. Este texto é usado para demonstrar o cálculo de frequência de palavras."
palavra = "texto"
frequencia = calcular_frequencia(texto, palavra)
print("A palavra '{}' aparece com frequência de {:.2f} no texto.".format(palavra, frequencia))
