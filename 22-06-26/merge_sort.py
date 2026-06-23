def mergesort(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result
arr = [6, 4, 8, 9, 3, 2, 5, 3, 4, 56, 77, 33, 88, 54, 73]
print(mergesort(arr))