def count_sort(arr):
    n=len(arr)
    if n<2:
        return arr
    #range of array
    min_val=min(arr)
    max_val=max(arr)
    range_array=max_val-min_val+1
    #count array and result array
    count_arr=[0]*range_array
    result=[0]*n
    #store count of entries
    for i in arr:
        count_arr[i-min_val]+=1
    #precedence sum array
    for i in range(1,len(count_arr)):
        count_arr[i]+=count_arr[i-1]
    #building the result array
    for num in reversed(arr):
        result[count_arr[num-min_val]-1]=num
        count_arr[num-min_val]-=1
    return result
arr=[3,4,5,2,3,5,6,1,2,4,5]
print(count_sort(arr))