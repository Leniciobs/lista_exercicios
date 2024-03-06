def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "As matrizes têm tamanhos diferentes e não podem ser somadas."
    
    resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        resultado.append(linha)
    
    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matriz1, matriz2)
if isinstance(resultado, str):
    print(resultado)
else:
    print("A soma das matrizes é:")
    for linha in resultado:
        print(linha)
