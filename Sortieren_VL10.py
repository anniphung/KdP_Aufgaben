#12.11.2025
#Kristin Knorr
#Rekursion und Suchalgorithmen

#Eingabe: [Int]
#Ausgabe: [Int]
#Voraussetzung: Elemente der Liste sind aus total geordnetem Universum
#Effekt: Liste ist im Anschluss aufsteigend sortiert
#Ergebnis: keins

#Selectionsort:
def min(xs,i):
    m = i
    for j in range(i+1,len(xs)):
        if xs[j]<xs[m]:
            m=j
    return m
    
def selectionSort(xs):
    for i in range(len(xs)):
        mini = min(xs,i)
        xs[mini],xs[i] = xs[i],xs[mini]

    
#Mergesort
def merge(left,right,xs):
    l=0
    r=0
    while l+r<len(xs):
        if l==len(left):
            xs[l+r]=right[r]
            r+=1
        elif r==len(right):
            xs[l+r]=left[l]
            l+=1
        elif left[l]<right[r]:
            xs[l+r]=left[l]
            l+=1
        else:
            xs[l+r]=right[r]
            r+=1
            
def mergeSort(xs):
    n=len(xs)
    if n<=1:
        return
    left = xs[:n//2]
    right = xs[n//2:n]
    mergeSort(left)
    mergeSort(right)
    merge(left,right,xs)


#Insertionsort
def insertSort(xs):
    for i in range(1,len(xs)):
        for j in range(i-1,-1,-1):
            if xs[i]<xs[j]:
                key = xs[i]
                xs[i]=xs[j]
                xs[j]=key
                i=i-1
            else:
                break
            
#Quicksort
def partition(xs, start,end):
    pivot = xs[start]
    l = start
    for i in range(start+1,end):
        if xs[i]<pivot:
            l +=1
            xs[i], xs[l] = xs[l],xs[i]
    xs[start], xs[l] = xs[l],xs[start]
    return l
    
def quicksort(xs):
    def quicksort_help (start,end):
        if (end-start)<=1:
            return
        split = partition(xs,start,end)
        quicksort_help(start,split)
        quicksort_help(split+1,end)
    quicksort_help(0,len(xs))
    
    
def quicksort2(xs):
    if len(xs)== 1 or len(xs)== 0:      #Rekursionsanker
        return xs
    else:
        pivot = xs[0]
        return quicksort2([x for x in xs[1:] if x<pivot])+ [pivot]+ quicksort2([x for x in xs[1:]if x>=pivot])
