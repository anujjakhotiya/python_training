class list_node:
    def __init__ (self,data):
        self.data=data
        self.next=None
    def show_node(self):
        print("data=",self.data,"next=",self.next)
n1=list_node(10)
n1.show_node()
n2=list_node(11)
n2.show_node()