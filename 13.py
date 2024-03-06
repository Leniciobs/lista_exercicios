def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return None

nome_arquivo = input("Digite o nome do arquivo a ser lido: ")
texto = ler_arquivo(nome_arquivo)
if texto:
    print("Conteúdo do arquivo:")
    print(texto)
