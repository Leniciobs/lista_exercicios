import csv

def soma_vendas_por_vendedor(nome_arquivo):
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
    
    return vendas_por_vendedor

nome_arquivo_csv = input("Digite o nome do arquivo CSV com os dados de vendas por vendedor: ")
vendas_por_vendedor = soma_vendas_por_vendedor(nome_arquivo_csv)
print("Soma de vendas por vendedor:")
for vendedor, soma_vendas in vendas_por_vendedor.items():
    print(f"{vendedor}: R$ {soma_vendas:.2f}")
