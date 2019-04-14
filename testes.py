# import sys
import csv
import random
import datetime as dt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import time

comp_quick = 0
troca_quick = 0

comp_merge = 0
troca_merge = 0

comp_heap = 0
troca_heap = 0

comp_shell =0
troca_shell =0

comp_select =0
troca_select=0

def quicksort(l):
    global comp_quick
    global troca_quick
    if l:
        comp_quick += 1
        left = [x for x in l if x < l[0]]
        comp_quick += 1
        right = [x for x in l if x > l[0]]
        if len(left) > 1:
            troca_quick += 1
            left = quicksort(left)
        if len(right) > 1:
            troca_quick += 1
            right = quicksort(right)
        return left + [l[0]] * l.count(l[0]) + right
    return []

def mergeSort(alist):    
    global comp_merge
    global troca_merge
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
            comp_merge +=1
            if lefthalf[i] < righthalf[j]:
                troca_merge += 1
                comp_merge += 1
                alist[k]=lefthalf[i]
                i=i+1
            else:
                troca_merge += 1
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
    global comp_heap
    global troca_heap
    for i in reversed(range(1, len(seq))):
        parent = (i - 1) // 2
        comp_heap += 1
        if seq[i] < seq[parent]:
            troca_heap += 1
            seq[i], seq[parent] = seq[parent], seq[i]

def shellSort(arr): 
    global comp_shell
    global troca_shell

    n = len(arr) 
    gap = n//2

    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i
            comp_shell += 1 
            while j >= gap and arr[j-gap] >temp: 
                troca_shell += 1
                arr[j] = arr[j-gap] 
                j -= gap  
            arr[j] = temp
            
            
        gap //= 2

# def auxShell(arr):
#     result = []
#     seq = list(arr)
#     while seq:
#         shellSort(seq)
#         result.append(seq.pop(0))
#     return result

def selectionSort(alist):
    global comp_select
    global troca_select
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            comp_select += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        troca_select += 1
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    

def auxSelect(alist):
    result = []
    seq = list(alist)
    while seq:
        selectionSort(seq)
        result.append(seq.pop(0))
    return result
    

nomes = []
sobrenomes = []

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
nome_completo_aux = []
tipo1 = []
while (n < int(max) ):
    sob = sobrenomes[random.randrange (len (sobrenomes))]
    nome = nomes[random.randrange( len (nomes))]
    nome_sob= nome+' '+sob
    nome_completo.append(nome_sob)
    nome_completo_aux.append(nome_completo)
    n += 1
else:
    print(nome_completo)
    menu = ''
    while (menu != '0') :
        print('\n\n 1 - Quick Sort,\n 2 - Merge Sort,\n 3 - Heap Sort,\n 4 - Shell Sort,\n 5 - Selection Sort \n 6- Original \n 0 - Fim teste')
        menu = input('Selecione uma opcao: ')
        if menu == '1':
            data_ini_quick = dt.datetime.now()
            tipo1 = quicksort(nome_completo)
            data_fim_quick = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000) 
            dif_quick = (data_fim_quick - data_ini_quick)

            print('\n LISTA: ',tipo1,'\n')

            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_quick)
            print('\n Tempo Final: ', data_fim_quick)
            print('\n Tempo Diferenca: ', dif_quick)
            print('\n Tempo Troca: ', troca_quick)
            print('\n Tempo Comparacao: ', comp_quick)
            
        elif menu == '2':
            data_ini_merge = dt.datetime.now()
            tipo2 = mergeSort(nome_completo)
            data_fim_merge = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_merge = data_fim_merge - data_ini_merge

            print('\n LISTA: ',tipo2,'\n')
            
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_merge)
            print('\n Tempo Final: ', data_fim_merge)
            print('\n Tempo Diferenca: ', dif_merge)
            print('\n Tempo Troca: ', troca_merge)
            print('\n Tempo Comparacao: ', comp_merge)

        elif menu == '3':
            data_ini_heap = dt.datetime.now()
            tipo3 = heap_sorted(nome_completo)
            data_fim_heap = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_heap = data_fim_heap - data_ini_heap

            print('\n LISTA: ',tipo3,'\n')
            
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_heap)
            print('\n Tempo Final: ', data_fim_heap)
            print('\n Tempo Diferenca: ', dif_heap)
            print('\n Tempo Troca: ', troca_heap)
            print('\n Tempo Comparacao: ', comp_heap)

        elif menu == '4':
            data_ini_shell = dt.datetime.now()
            # tipo4 = auxShell(nome_completo)
            shellSort(nome_completo)
            data_fim_shell = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_shell = data_fim_shell - data_ini_shell

            # print('\n LISTA: ',tipo4,'\n')
            print('\n',nome_completo,'\n')
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_shell)
            print('\n Tempo Final: ', data_fim_shell)
            print('\n Tempo Diferenca: ', dif_shell)
            print('\n Tempo Troca: ', troca_shell)
            print('\n Tempo Comparacao: ', comp_shell)

        elif menu == '5':
            data_ini_select = dt.datetime.now()
            tipo5 = auxSelect(nome_completo)
            # selectionSort(nome_completo)
            data_fim_select = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_select = data_fim_select - data_ini_select

            print('\n LISTA: ',tipo5,'\n')
            # print('\n ',nome_completo)
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_select)
            print('\n Tempo Final: ', data_fim_select)
            print('\n Tempo Diferenca: ', dif_select)
            print('\n Tempo Troca: ', troca_select)
            print('\n Tempo Comparacao: ', comp_select)

        elif menu == '6':
            print('\n',nome_completo,'\n')
        else:
            print('\n Numero Invalido')
    else:
        print('\n\n Finalizando testes')





# quick = pd.DataFrame({
#             'Metodo':['Quick Sort'],
#             'Qtd Dados':[max],
#             'Tempo Inicial':[data_ini_quick],
#             'Tempo Final': [data_fim_quick],
#             'Diferenca': [dif_quick],
#             'Troca': [troca_quick],
#             'Comparacoes':[troca_quick]
#             })
#             writer = ExcelWriter('QuickSort.xlsx')
#             quick.to_excel(writer,'Sheet1',index=False)
#             writer.save()

#https://wiki.python.org.br/QuickSort
#https://www.pythoncentral.io/merge-sort-implementation-guide/
#https://codereview.stackexchange.com/questions/194062/heap-sort-implementation-in-python
#https://www.geeksforgeeks.org/shellsort/
#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html