from shorts import Shorts
import csv
import random
import datetime as dt
import numpy as np
import time

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

def geraNomes(max, nomes, sobrenomes):
    nome_completo = []
    n = 0
    while ( n < int(max)  ):
        sob = sobrenomes[random.randrange (len(sobrenomes))]
        nome = nomes[random.randrange( len (nomes))]
        nome_completo.append(nome+' '+sob)
        n += 1
    return nome_completo

def menuPrincipal(nomes, sobrenomes):
    while True:
        print('\nOpcoes:')
        print('\n0- finalizar o programa')  
        print('\n1-Iniciar\n')
        ini = input()
        if (int(ini) == 1):
            max = input('\nNumero da massa de dados:')
            nome_completo = []
            nome_completo = list(geraNomes(max, nomes, sobrenomes))
            menuShorts(max,nome_completo)
        else:
            return

def menuShorts(max,nome_completo):
    while True :
        s = Shorts()
        print('\n 1 - Quick Sort,\n 2 - Merge Sort,\n 3 - Heap Sort,\n 4 - Shell Sort,\n 5 - Selection Sort \n 6- Original \n 0 - Fim ')
        menu = input('Selecione uma opcao: ')
        if menu == '1':
            data_ini_quick = dt.datetime.now()
            tipo1 = s.quicksort(nome_completo)
            data_fim_quick = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000) 
            dif_quick = (data_fim_quick - data_ini_quick)

            print('\n LISTA: ',tipo1,'\n')
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_quick)
            print('\n Tempo Final: ', data_fim_quick)
            print('\n Tempo Diferenca: ', dif_quick)
            print('\n Tempo Troca: ', s.troca_quick)
            print('\n Tempo Comparacao: ', s.comp_quick)
            
        elif menu == '2':
            data_ini_merge = dt.datetime.now()
            tipo2 = s.mergeSort(nome_completo)
            data_fim_merge = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_merge = data_fim_merge - data_ini_merge

            print('\n LISTA: ',tipo2,'\n')
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_merge)
            print('\n Tempo Final: ', data_fim_merge)
            print('\n Tempo Diferenca: ', dif_merge)
            print('\n Tempo Troca: ', s.troca_merge)
            print('\n Tempo Comparacao: ', s.comp_merge)

        elif menu == '3':
            data_ini_heap = dt.datetime.now()
            tipo3 = s.heap_sorted(nome_completo)
            data_fim_heap = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_heap = data_fim_heap - data_ini_heap

            print('\n LISTA: ',tipo3,'\n')
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_heap)
            print('\n Tempo Final: ', data_fim_heap)
            print('\n Tempo Diferenca: ', dif_heap)
            print('\n Tempo Troca: ', s.troca_heap)
            print('\n Tempo Comparacao: ', s.comp_heap)

        elif menu == '4':
            data_ini_shell = dt.datetime.now()
            tipo4 = s.shellSort(nome_completo)
            data_fim_shell = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_shell = data_fim_shell - data_ini_shell
            print('\n LISTA: ',tipo4,'\n')
            print('\n',nome_completo,'\n')
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_shell)
            print('\n Tempo Final: ', data_fim_shell)
            print('\n Tempo Diferenca: ', dif_shell)
            print('\n Tempo Troca: ', s.troca_shell)
            print('\n Tempo Comparacao: ', s.comp_shell)

        elif menu == '5':
            data_ini_select = dt.datetime.now()
            tipo5 = s.selectionSort(nome_completo)
            data_fim_select = dt.datetime.now()
            dt.timedelta(-1, 86392, 895000)
            dif_select = data_fim_select - data_ini_select

            print('\n LISTA: ',tipo5,'\n')
            print('\n Massa de dados: ', max)
            print('\n Tempo Inicial: ', data_ini_select)
            print('\n Tempo Final: ', data_fim_select)
            print('\n Tempo Diferenca: ', dif_select)
            print('\n Tempo Troca: ', s.troca_select)
            print('\n Tempo Comparacao: ', s.comp_select)
        elif menu == '6':
            print('\n Original: ',nome_completo,'\n')
        elif menu == '0':
            return

menuPrincipal(nomes, sobrenomes)


        
