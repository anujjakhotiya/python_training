import time
def bubble(arr):
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n - 1):
        for j in range(n - 1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr   
                       
print(bubble([1,6,4,7,8,4,9]))
print(bubble(['a','z','x']))


def optimal_bubble(arr) :
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


optimal_start = time.time()
print(optimal_bubble([1,6,4,7,8,4,9]))
print(optimal_bubble(['a','z','x']))
optimal_end = time.time()
print(f"{optimal_start:.6f} seconds"    )
print(f"{optimal_end - optimal_start:.6f} seconds")