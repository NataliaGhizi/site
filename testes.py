# import sys
import csv
import random
import datetime as dt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

def quicksort(l):
        if l:
                left = [x for x in l if x < l[0]]
                right = [x for x in l if x > l[0]]
                if len(left) > 1:
                        left = quicksort(left)
                if len(right) > 1:
                        right = quicksort(right)
                return left + [l[0]] * l.count(l[0]) + right
        return []

def mergeSort(alist):

#    print("Splitting ",alist)
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   return alist

def heap_sorted(iterable):
    result = []
    seq = list(iterable)
    while seq:
        heapify(seq)
        result.append(seq.pop(0))
    return result

def heapify(seq):
    for i in reversed(range(1, len(seq))):
        parent = (i - 1) // 2
        if seq[i] < seq[parent]:
            seq[i], seq[parent] = seq[parent], seq[i]

def shellSort(arr): 
	n = len(arr) 
	gap = n//2

	while gap > 0: 
		for i in range(gap,n): 
			temp = arr[i] 
			j = i 
			while j >= gap and arr[j-gap] >temp: 
				arr[j] = arr[j-gap] 
				j -= gap  
			arr[j] = temp 
            
		gap //= 2

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

nomes = []
sobrenomes = []
data_ini = []
data_fim = []
dif = []

with open('arq/nomes.csv', newline='') as f:
    arq = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    count = 0
    for row in arq:
        nomes.append(row[count])
        count += count
with open('arq/sobrenomes.csv', newline='') as f:
    arq = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    count = 0
    for row in arq:
        sobrenomes.append(row[count])
        count += count
# max = 10
n = 0
max = input('\n Numero da massa de dados:')
nome_completo = []
tipo1 = []
while (n < int(max) ):
    sob = sobrenomes[random.randrange (len (sobrenomes))]
    nome = nomes[random.randrange( len (nomes))]
    nome_sob= nome+' '+sob
    nome_completo.append(nome_sob)
    n += 1
else:
    print(nome_completo)
    print('\n\n 1 - Quick Sort,\n 2 - Merge Sort,\n 3 - Heap Sort,\n 4 - Shell Sort,\n 5 - Selection Sort. \n 0 - Fim teste')
    menu = input('Selecione uma opcao: ')
    if menu == '1':
        data_ini_quick = dt.datetime.now()
        tipo1 = quicksort(nome_completo)
        data_fim_quick = dt.datetime.now()
        dt.timedelta(-1,0,999999) 
        dif_quick = data_fim_quick - data_ini_quick
        # dif = divmod(data_ini[0],data_fim[0])
        print('\n\n',tipo1)
        print('\n\n',dif_quick)
        print('\n\n',data_ini_quick)
        print('\n\n',data_fim_quick)
    elif menu == '2':
        data_ini_merge = dt.datetime.now()
        tipo2 = mergeSort(nome_completo)
        data_fim_merge = dt.datetime.now()
        dt.timedelta(-1,0,999999)
        dif_merge = data_fim_merge - data_ini_merge
        print('\n\n', tipo2)
        print('\n\n',dif_merge)
        print('\n\n',data_ini_merge)
        print('\n\n',data_fim_merge)
    elif menu == '3':
        data_ini_heap = dt.datetime.now()
        tipo3 = heap_sorted(nome_completo)
        data_fim_heap = dt.datetime.now()
        dt.timedelta(-1,0,999999)
        dif_heap = data_fim_heap - data_ini_heap
        print('\n\n', tipo3)
        print('\n\n',dif_heap)
        print('\n\n',data_ini_heap)
        print('\n\n',data_fim_heap)
    elif menu == '4':
        data_ini_shell = dt.datetime.now()
        shellSort(nome_completo)
        data_fim_shell = dt.datetime.now()
        dt.timedelta(-1,0,999999)
        dif_shell = data_fim_shell - data_ini_shell
        print('\n\n',nome_completo)
    elif menu == '5':
        data_ini_select = dt.datetime.now()
        selectionSort(nome_completo)
        data_fim_select = dt.datetime.now()
        dt.timedelta(-1,0,999999)
        dif_select = data_fim_select - data_ini_select
        print('\n\n',nome_completo)
    else:
        print('\n\n Finalizando testes')
        df = pd.DataFrame({
            'Metodo':[1,2,3],
            'Qtd Dados':[1,2,3],
            'Tempo Inicial':[1,2,3],
            'Tempo Final': [1,2,3],
            'Diferenca': [1,2,3],
            'Memoria': [1,2,3],
            'Processador':[1,2,3]
        })
        writer = ExcelWriter('analiseShorts.xlsx')
        df.to_excel(writer,'Sheet1',index=False)
        writer.save()


#https://wiki.python.org.br/QuickSort
#https://www.pythoncentral.io/merge-sort-implementation-guide/
#https://codereview.stackexchange.com/questions/194062/heap-sort-implementation-in-python
#https://www.geeksforgeeks.org/shellsort/
#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html