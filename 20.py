import csv

def vendedor_mais_menos_vendeu(nome_arquivo):
    vendas_por_vendedor = {}
    
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)  
        
        for linha in leitor_csv:
            vendedor, venda = linha
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += float(venda)
            else:
                vendas_por_vendedor[vendedor] = float(venda)
    
    vendedor_mais_vendeu = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
    vendedor_menos_vendeu = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
    
    return vendedor_mais_vendeu, vendedor_menos_vendeu

nome_arquivo_csv = input("Digite o nome do arquivo CSV com os dados de vendas por vendedor: ")
vendedor_mais_vendeu, vendedor_menos_vendeu = vendedor_mais_menos_vendeu(nome_arquivo_csv)
print("Vendedor que mais vendeu:", vendedor_mais_vendeu)
print("Vendedor que menos vendeu:", vendedor_menos_vendeu)
