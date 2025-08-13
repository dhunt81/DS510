# Prof. K
# DS 510
# Assignment 09 Quicksort KEY, with partition

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x :
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[r]
    A[r] = A[i+1]
    A[i+1] = temp
    return i + 1

def quicksort(A,p,r):
    if p < r:
        q  = partition(A , p , r)
        quicksort(A , p , q-1)
        quicksort(A , q+1 , r)


