'''pattern: 
1
23
456
78910
1112131415'''
n=int(input())
for i in range (1,n):
    for j in range (1,i+1):
        print(j,end="")
    print()