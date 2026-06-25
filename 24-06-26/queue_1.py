from collections import deque
Q=deque()
def PushQ(Q,val):
    Q.append(val)
def PopQ(Q):
    if Q:
        return Q.popleft()
    else:
        print("Queue is empty")
def seekQ(Q):
    if Q:
        return Q[0]
    else:
        print("Queue is empty")
        return
PushQ(Q,0)
PushQ(Q,1)
PushQ(Q,2)
print(seekQ(Q))
print(PopQ(Q))