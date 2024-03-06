import os

def consolidar_arquivos(diretorio_origem, nome_arquivo_destino):
    with open(nome_arquivo_destino, 'w') as arquivo_destino:
        for nome_arquivo in os.listdir(diretorio_origem):
            if nome_arquivo.endswith('.txt'):
                caminho_arquivo = os.path.join(diretorio_origem, nome_arquivo)
                with open(caminho_arquivo, 'r') as arquivo_origem:
                    conteudo = arquivo_origem.read()
                    arquivo_destino.write(conteudo)
                    arquivo_destino.write('\n')

diretorio_origem = input("Digite o caminho do diretório com os arquivos de texto: ")
nome_arquivo_destino = input("Digite o nome do arquivo consolidado: ")
consolidar_arquivos(diretorio_origem, nome_arquivo_destino)
print("Arquivos consolidados com sucesso no arquivo:", nome_arquivo_destino)
