def sb_linear(arr,target):
    for _ in arr:
        if _ == target:
            return arr.index(_)
    return -1
s_list=[3,4,5,3,2,4,6,7,4,2]
target=2
print(sb_linear(s_list,target))

def m_c_linear(arr,target):
    count=0
    for _ in arr:
        if _ == target:
            count+=1
    return -1 if count==0 else count
s_list=[3,4,5,3,2,4,6,7,4,2]
target=4
print(m_c_linear(s_list,target))

def m_i_linear(arr,target):
    count=[]
    for _ in range(len(arr)):
        if arr[_] == target:
            count.append((_))
    return count
s_list=[3,4,5,3,2,4,6,7,4,2]
target=3
print(m_i_linear(s_list,))