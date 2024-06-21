class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value <= self.val:
            if self.left:
                self.left.insert(new_value)
            else:
                self.left = Node(new_value)
        else:
            if self.right:
                self.right.insert(new_value)
            else:
                self.right = Node(new_value)

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.val)
        if self.right:
            self.right.print_inorder()

    def contains(self, value_to_find):
        if value_to_find == self.val:
            return True
        if value_to_find < self.val:
            if self.left:
                return self.left.contains(value_to_find)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value_to_find)
            else:
                return False


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def print_inorder(self):
        if self.root:
            self.root.print_inorder()

    def contains(self, value):
        if self.root:
            return self.root.contains(value)
        return False

array = [1,2,3,4,5,6,7,8,9]
tree = Tree()
for i in array:
    tree.insert(i)
tree.print_inorder()
print(tree.contains(9))
print(tree.contains(11))
