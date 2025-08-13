# Prof. K
# DS 510
# Assignment 09 Mergesort KEY, with merge

def merge (A,p,q,r):
    # much slower to calculate infinity via max
    #infinity = max(A)+5
    infinity = 1000000
    L = []
    R = []
    n1 = q-p+1
    n2 = r-q
    for i in range(n1):
       L.append( A[p+i] )
    for j in range(n2):
       R.append( A[q+j+1] )
    L.append( infinity )
    R.append( infinity )
    i=0
    j=0
    for k in range(p,r+1):
       if L[i] <= R[j]:
           A[k] = L[i]
           i += 1
       else:
           A[k] = R[j]
           j += 1

def mergesort(A,p,r):
    if p < r:
       q  = (p+r)//2
       mergesort(A,p,q)
       mergesort(A,q+1,r)
       merge(A,p,q,r)
