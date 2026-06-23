def quicksort(arr):
    n=len(arr)
    if n<2:
        return arr
    else:
        pivot=arr[n//2]
        left=[x for x in arr if x<pivot]
        middle=[x  for x in arr if x==pivot]
        right=[x for x in arr if x>pivot]
        return quicksort(left)+middle+quicksort(right)
arr=[2,3,6,7,6,4,2,6,5,7,8,9,6,4,5,3,78,3,2]
print(quicksort(arr))