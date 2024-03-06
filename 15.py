import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados_json = json.load(arquivo)
        return dados_json
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print("O arquivo JSON está formatado incorretamente.")
        return None

nome_arquivo_json = input("Digite o nome do arquivo JSON a ser lido: ")
dados_json = ler_arquivo_json(nome_arquivo_json)
if dados_json:
    print("Conteúdo do arquivo JSON:")
    print(dados_json)
