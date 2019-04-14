class Shorts:
    def __init__(self):
        self.nome_completo = []
        self.comp_quick = 0
        self.troca_quick = 0
        self.comp_merge = 0
        self.troca_merge = 0
        self.comp_heap = 0
        self.troca_heap = 0
        self.comp_shell = 0
        self.troca_shell = 0
        self.comp_select = 0
        self.troca_select = 0

    def quicksort(self, l):
        if l:
            self.comp_quick += 1
            left = [x for x in l if x < l[0]]
            self.comp_quick += 1
            right = [x for x in l if x > l[0]]
            if len(left) > 1:
                self.troca_quick += 1
                left = self.quicksort(left)
            if len(right) > 1:
                self.troca_quick += 1
                right = self.quicksort(right)
            return left + [l[0]] * l.count(l[0]) + right
        return []

    def mergeSort(self, l):
        alist = []
        alist = list(l)     
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            #recursion
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i,j,k=0, 0, 0
            while i < len(lefthalf) and j < len(righthalf):
                self.comp_merge +=1
                if lefthalf[i] < righthalf[j]:
                    self.troca_merge += 1
                    self.comp_merge += 1
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    self.troca_merge += 1
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

    def heap_sorted(self, iterable):
        result = []
        seq = list(iterable)
        while seq:
            self.heapify(seq)
            result.append(seq.pop(0))
        return result

    def heapify(self, seq):
        for i in reversed(range(1, len(seq))):
            parent = (i - 1) // 2
            self.comp_heap += 1
            if seq[i] < seq[parent]:
                self.troca_heap += 1
                seq[i], seq[parent] = seq[parent], seq[i]

    def shellSort(self, l): 
        arr = []
        arr = list(l)
        n = len(arr) 
        gap = n//2

        while gap > 0: 
            for i in range(gap,n): 
                temp = arr[i] 
                j = i
                self.comp_shell += 1 
                while j >= gap and arr[j-gap] >temp: 
                    self.troca_shell += 1
                    arr[j] = arr[j-gap] 
                    j -= gap  
                arr[j] = temp
 
            gap //= 2
        return arr

    def selectionSort(self, l):
        alist = []
        alist = list(l)

        for fillslot in range(len(alist)-1,0,-1):
            positionOfMax=0
            for location in range(1,fillslot+1):
                self.comp_select += 1
                if alist[location] > alist[positionOfMax]:
                    positionOfMax = location
            self.troca_select += 1
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
        return alist

