import csv

def mes_mais_vendas(nome_arquivo):
    vendas_por_mes = {}
    
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv) 
        
        for linha in leitor_csv:
            mes, vendas = linha
            if mes in vendas_por_mes:
                vendas_por_mes[mes] += float(vendas)
            else:
                vendas_por_mes[mes] = float(vendas)
    
    mes_mais_vendido = max(vendas_por_mes, key=vendas_por_mes.get)
    return mes_mais_vendido

nome_arquivo_csv = input("Digite o nome do arquivo CSV com os dados de vendas por mês: ")
mes_mais_vendido = mes_mais_vendas(nome_arquivo_csv)
print("O mês com mais vendas foi:", mes_mais_vendido)
