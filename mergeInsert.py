#Insertionsort
def insertSort(xs):
    for i in range(1,len(xs)):
        print(xs)
        for j in range(i-1,-1,-1):
            if xs[i]<xs[j]:
                key = xs[i]
                xs[i]=xs[j]
                xs[j]=key
                i=i-1
            else:
                break

#MergeInsertsort
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
            
def mergeInsertSort(xs, k):
    print(xs)
    n=len(xs)
    if n <= k:
        return insertSort(xs)
    else:
        left = xs[:n//2]
        right = xs[n//2:n]
        mergeInsertSort(left, k)
        mergeInsertSort(right, k)
        merge(left,right,xs)

xs = [3,2,1,5,3,5,4,8,4,12,23,25,1,2]
#print(mergeInsertSort(xs , 5))
print(xs[0])
