import csv

arquivo = open('arq/nomes.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha,'\n')