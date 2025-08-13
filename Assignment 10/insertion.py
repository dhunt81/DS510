# Prof. K
# DS 510
# Assignment 09 Insertion Sort KEY

def insertion(A):
    n = len(A)
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i -= 1
        A[i+1] = key