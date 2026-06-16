a=[1,2,3,4,5,6,7,8,9,10]
max=0;
for i in range (0,len(a)):
    if (a[i]>max):
        max=a[i]
print(max)
sum=0
for i in range (0,len(a)):
    sum=sum+a[i]
print(sum)
#second largest
max=0
secondmax=0
for i in range (0,len(a)):
    if (a[i]>max):
        secondmax=max
        max=a[i]
    elif (a[i]>secondmax and a[i]!=max):
        secondmax=a[i]
print(secondmax)
#reverse of array
reverse=[]
for i in range (len(a)-1,-1,-1):
    reverse.append(a[i])
print(reverse)
a.insert(0,11)
print(a)
a.insert(10,12)
print(a)
#ascending order
for i in range (0,len(a)):
    for j in range (i+1,len(a)):
        if (a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
#descending order
for i in range (0,len(a)):
    for j in range (i+1,len(a)):
        if (a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
