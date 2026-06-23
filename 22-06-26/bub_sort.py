#bubble sort
def bubsort(arr):
    n=len(arr)
    if n<2:
        return arr
    for i in range(n-1):
        for j in range(n-1-i):
            if  arr[j]>arr[j+1]:#if we use >= algo will become unstable
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
#arr=[3,1,2,4,0]
print(bubsort(arr=[3,1,4,2,4,0]))
#optimal bubblesort and flagging
def optimalbubsort(arr):
    n=len(arr)
    if n<2:
        return arr
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if  arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
#arr=[3,1,2,4,0]
print(optimalbubsort(arr=[3,1,4,2,4,0]))

#descending
def optimalbubsort(arr):
    n=len(arr)
    if n<2:
        return arr
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if  arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
#arr=[3,1,2,4,0]
print(optimalbubsort(arr=[3,1,4,2,4,0]))

import time
arr=[1,2,5,8,2,2,2,5,6,7,8,90,4]
normal_start=time.time()
bubsort(arr)
print("Total time: ",time.time()-normal_start)
arr=[1,2,5,8,2,2,2,5,6,7,8,90,4]
optimal_start=time.time()
bubsort(arr)
print("Total time: ",time.time()-optimal_start)
