class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class Doubly_Linked_List:
    def __init__(self):
        self.head=None
    def insert_at_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node 
    def insert_at_tail(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
    def insert_at_index(self,val,index):
        new_node=Node(val)
        if not head:
            return
        curr=self.head
        for i in range(index-1):
            if curr.next:
                curr=curr.next
            return
        #temp=curr.next
        new_node.prev=curr
        new_node.next=curr.next
        curr.next=new_node
        new_node.next.prev=new_node
    def delete_at_head(self):
        if self.head:
            self.head=self.head.next
            if head:
                self.head.prev=None
        else:
            return
    def delete_at_tail(self):
        if not self.head:
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.prev.next=None
    def delete_by_value(self,val):
        if not self.head:
            return
        #Value is at head
        if self.head.val==val:
            self.head=self.head.next
            if head:
                self.head.prev=None
            return
        #Value in middle or at tail
        curr=self.head
        while curr and curr.val!=val:
            curr=curr.next
        #value is found
        if curr:  #If the list still exsists
            if curr.next:   #Node is in middle
                curr.next.prev=curr.prev
            if curr.prev:
                    curr.prev.next= curr.next