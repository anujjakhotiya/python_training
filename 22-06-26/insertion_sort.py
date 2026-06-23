def insertion_sort(arr):
  n=len(arr)
  if n<2:
    return arr
  for i in range(1,len(arr)):
      key=arr[i]
      j=i-1
      while(j>=0 and key<arr[j]):
         arr[j+1]=arr[j]
         j-=1
      arr[j+1]=key
  return arr
arr=[2,5,6,4,2,3,6,3,9,8,5,9,6,8]
print(insertion_sort(arr))