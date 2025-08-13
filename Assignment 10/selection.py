# Prof. K
# DS 510
# Assignment 09 Selection Sort KEY

def selection(A):
    for i in range(len(A)):
        smallestLocation = i
        for j in range(i+1,len(A)):
            if A[smallestLocation] > A[j]:
                smallestLocation = j
        # Swap A[i] with A[smallestLocation]
        temp = A[i]
        A[i] = A[smallestLocation]
        A[smallestLocation] = temp
