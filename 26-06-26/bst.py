class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_in_BST(self, curr, val):
        if self.root is None:
            self.root = Node(val)
            return

        if val < curr.val:
            if curr.left is None:
                curr.left = Node(val)
            else:
                self.insert_in_BST(curr.left, val)
        else:
            if curr.right is None:
                curr.right = Node(val)
            else:
                self.insert_in_BST(curr.right, val)

    def search_in_BST(self, curr, val):
        if curr is None:
            return False
        if curr.val == val:
            return True
        if val < curr.val:
            return self.search_in_BST(curr.left, val)
        return self.search_in_BST(curr.right, val)

    def inorder(self, curr):
        if curr is None:
            return
        self.inorder(curr.left)
        print(curr.val, end=" ")
        self.inorder(curr.right)