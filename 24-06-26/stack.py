def Push(stk,val):
    global top
    top+=1
    stk.append(val)

def Pop(stk):
    global top
    if not IsEmpty(stk):
        print("Last element is removed!!!")
        top-=1
        return stk.pop()
    
def Peek(stk):
    global top
    if not IsEmpty(stk):
        return stk[top]
    else:
        print("Stack is empty")

def IsEmpty(stk):
    global top
    return top==-1

top=-1
stack=[]
print(Peek(stack))
Push(stack,0)
Push(stack,1)
Push(stack,2)
print(Peek(stack))
print(Pop(stack))
print(Peek(stack))