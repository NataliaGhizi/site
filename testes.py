import csv
import random
nomes = []
sobrenomes = []
with open('arq/nomes.csv', newline='') as f:
    arq = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    count = 0
    for row in arq:
        nomes.append(row[count])
        count = + count
with open('arq/sobrenomes.csv', newline='') as f:
    arq = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    count = 0
    for row in arq:
        sobrenomes.append(row[count])
        count = + count

print(nomes[random.randrange( len (nomes))] , sobrenomes[random.randrange (len (sobrenomes))] )