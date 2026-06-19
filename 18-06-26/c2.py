def add_item(item,bag=[]):
    bag.append(item)
    return bag
food=["cake","bread"]
print(add_item("apple"))
print(add_item("kiwi"))
print(add_item("mango",food))

funcs=[]
for i in range(5):
    funcs.append(lambda:i*i)
print(funcs)
