import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='') as arquivo:
            leitor_csv = csv.reader(arquivo)
            linhas = list(leitor_csv)
        return linhas
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return None

nome_arquivo_csv = input("Digite o nome do arquivo CSV a ser lido: ")
dados_csv = ler_arquivo_csv(nome_arquivo_csv)
if dados_csv:
    print("Conteúdo do arquivo CSV:")
    for linha in dados_csv:
        print(linha)
