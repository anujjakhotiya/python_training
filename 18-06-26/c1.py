'''def counter():
    count=0
    def step():
        count+=1
        return count
    return step()
c=counter()
print(c)'''
'''if you run j in dictionary , j will be recognized only and
only if it is one of the keys in the dict..
the values r not  directly acccesed by in operator '''
import builtins
print(type(builtins.len))
print("len" in dir(builtins))