class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SkewMinHeap:
    def __init__(self):
        self._size = 0
        self.root = None

    def count(self):
        print(self._size)

    def top(self):
        if self.root is None:
            print("ERROR: Heap is empty.")
        else:
            print(self.root.value)

    def push(self, value):
        self.root = self.merge(self.root, Node(value))
        self._size += 1

    def pop(self):
        if self.root is None:
            print("ERROR: Heap is empty.")
        else:
            print(self.root.value)
            self.root = self.merge(self.root.left, self.root.right)
            self._size -= 1

    def merge(self, leftTree, rightTree):
        if leftTree is None:
            return rightTree
        if rightTree is None:
            return leftTree

        if leftTree.value > rightTree.value:
            leftTree, rightTree = rightTree, leftTree

        leftTree.left, leftTree.right = leftTree.right, leftTree.left
        leftTree.right = self.merge(rightTree, leftTree.right)
        return leftTree
    
    def print(self):
        if self.root is None:
            print("ERROR: Heap is empty.")
        else:
            print(self._recursivePrint(self.root))

    def _recursivePrint(self, node):
        if node is None:
            return "-"
        if node.left is None and node.right is None:
            return str(node.value)
        return "(" + self._recursivePrint(node.left) + " " + str(node.value) + " " + self._recursivePrint(node.right) + ")"
        
