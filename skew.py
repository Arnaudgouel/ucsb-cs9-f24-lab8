class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SkewMinHeap:
    def __init__(self):
        self._size = 0
        self._root = None

    def count(self):
        print(self._size)

    def top(self):
        if self._root is None:
            print("ERROR: Heap is empty.")
        else:
            print(self._root.value)
            print(self._root.left.value)
            print(self._root.right.value)

    def push(self, value):
        self._root = self._merge(self._root, Node(value))
        self._size += 1

    def pop(self):
        if self._root is None:
            print("ERROR: Heap is empty.")
        else:
            print(self._root.value)
            self._root = self._merge(self._root.left, self._root.right)
            self._size -= 1

    def _merge(self, leftTree, rightTree):
        if leftTree is None:
            return rightTree
        if rightTree is None:
            return leftTree

        if leftTree.value > rightTree.value:
            leftTree, rightTree = rightTree, leftTree

        leftTree.right = self._merge(leftTree.right, rightTree)
        leftTree.left, leftTree.right = leftTree.right, leftTree.left
        return leftTree
    
    def print(self):
        if self._root is None:
            print("ERROR: Heap is empty.")
        else:

            print("("+self._recursivePrint(self._root)+")")

    def _recursivePrint(self, node):
        if node is None:
            return "-"
        if node.left is None and node.right is None:
            return str(node.value)
        return self._recursivePrint(node.left) + " " + str(node.value) + " " + self._recursivePrint(node.right)
        
