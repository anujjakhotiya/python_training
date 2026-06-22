l1=list([])
l1.append(10)
print(l1)
l1.extend([20,30,40,50])
print(l1)
l1.append([70,80,90])
print(l1)
l1.insert(0,0)
print(l1)
l1.append((100,120))
print(l1)
for i in range (len(l1)):
    if l1[i]==0:
        l1[i]=1
for _ in (l1):
    print(_)     
l2=[11,2,3,2,3,4,1,2,3,3,3,4]
print(l2.count(3))
print(l2.count(4))
print(l2.count(1))
l3=[30,40,10,20,60]
print(sorted(l3))
print(l3)