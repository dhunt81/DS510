##################################
### Created: August 10, 2025
### Author: Devin Hunt
### DS510 Assignment 10 Part B
### Description: Timing for different sort algorithms
### Inputs: Size of sorted terms
### Packages: None
### Output: console output
### References: Dr. Kruse's code for starting this code driver
##################################

from selection import *
from mergesort import *
from insertion import *
from quicksort import *
import time

import random

import sys
sys.setrecursionlimit(200000) # Increase the limit to 2000

# Define function to run a sort based on the selection of sort type. Returns the time to conduct sort
def runSorts(x, sort):
    sort_start = time.perf_counter()
    #create copies of list as the sorts return the original list sorted
    a = x[:]
    b = x[:]
    c = x[:]
    d = x[:]  

    if sort == 1:
        print("Select Sort")
        selection(a)
    elif sort == 2:
        print("Merge Sort")
        mergesort(b,0,n-1)
    elif sort == 3:
        print("Insert Sort")
        insertion(c)
    elif sort ==4:
        print("Quick Sort")
        quicksort(d,0,n-1)
    else:
        print("Already Sorted")
        x.sort()
    sort_end = time.perf_counter()
    sort_time = sort_end - sort_start

    return (sort_time)

    
if __name__ == "__main__":
    n = int(input("Enter the size: "))
#    sort = int(input("1-Selection\n\
#2-Mergesort\n\
#3-Insertion\n\
#4-Quicksort\n\
#5-Built-In\n\
#: "))

    # Get a random list of elements
    x = []
    for i in range(0,n):
        x.append(random.randint(0,n))

    #Execute all 4 sorting methods

    for i in range(1,5):
        # Run sorting algorithm
        timing = runSorts(x, i)

        isSorted = x == sorted(x)
        print(f'sorted? {isSorted}\nTime to sort: {timing}')


""" Outputs Testing

>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 10\\Assignment 10B - Hunt.py"
Enter the size: 
1000
Select Sort
sorted? False
Time to sort: 0.009498400148004293
Merge Sort
sorted? False
Time to sort: 0.0013213001657277346
Insert Sort
sorted? False
Time to sort: 0.008635799866169691
Quick Sort
sorted? False
Time to sort: 0.00044810003601014614
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 10\\Assignment 10B - Hunt.py"
Enter the size: 
5000
Select Sort
sorted? False
Time to sort: 0.2326221999246627
Merge Sort
sorted? False
Time to sort: 0.00541809992864728
Insert Sort
sorted? False
Time to sort: 0.23463730001822114
Quick Sort
sorted? False
Time to sort: 0.002823400078341365
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 10\\Assignment 10B - Hunt.py"
Enter the size: 
100000
Select Sort
sorted? False
Time to sort: 106.57582209981047
Merge Sort
sorted? False
Time to sort: 0.1643391998950392
Insert Sort
sorted? False
Time to sort: 105.43076659995131
Quick Sort
sorted? False
Time to sort: 0.07772849989123642
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 10\\Assignment 10B - Hunt.py"
Enter the size: 
200000
Select Sort
sorted? False
Time to sort: 428.9607632001862
Merge Sort
sorted? False
Time to sort: 0.2889620999339968
Insert Sort
sorted? False
Time to sort: 414.3944860000629
Quick Sort
sorted? False
Time to sort: 0.19010909995995462
>>>

"""


    
