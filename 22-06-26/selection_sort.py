def selectionsort(arr):
  n=len(arr)
  if n<2:
    return arr
  for i in range(n-1):
    smallest=i
    for j in range(i+1,n):
      if arr[j]<arr[smallest]:
        smallest=j
    arr[i],arr[smallest]=arr[smallest],arr[i]
  return arr
arr=[2,5,6,4,2,3,6,3,9,8,5,9,6,8]
print(selectionsort(arr))