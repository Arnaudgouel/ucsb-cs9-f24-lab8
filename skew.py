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
        return self._size

    def top(self):
        if self.root is None:
            return "ERROR: Heap is empty."
        else:
            return self.root.value

    def push(self, value):
        self.root = self.merge(self.root, Node(value))
        self._size += 1

    def pop(self):
        if self.root is None:
            return "ERROR: Heap is empty."
        else:
            temp = self.root.value
            self.root = self.merge(self.root.left, self.root.right)
            self._size -= 1
            return temp
        
    def getSpine(self, root):
        spine = []
        current = root
        while current:
            spine.append(current)
            current = current.left
        return spine

    def merge(self, leftTree, rightTree):
        if leftTree is None:
            return rightTree
        if rightTree is None:
            return leftTree
        
        leftSpine = self.getSpine(leftTree)
        rightSpine = self.getSpine(rightTree)

        i = 0
        j = 0
        result = None
        nextNode = None
        last = None

        while i < len(leftSpine) and j < len(rightSpine):
            left = leftSpine[i]
            right = rightSpine[j]

            if left.value <= right.value:
                nextNode = left
                i += 1
            else:
                nextNode = right
                j += 1
            
            if not result:
                result = nextNode
            else:
                last.left = nextNode
            last = nextNode
        
        while i < len(leftSpine):
            if not result:
                result = leftSpine[i]
            else:
                last.left = leftSpine[i]
            last = leftSpine[i]
            i += 1

        while j < len(rightSpine):
            if not result:
                result = rightSpine[j]
            else:
                last.left = rightSpine[j]
            last = rightSpine[j]
            j += 1

        current = result
        while current:
            next = current.left
            current.left, current.right = current.right, current.left
            current = next

        return result
    

    def print(self):
        print(self._recursivePrint(self.root))

    def _recursivePrint(self, node):
        if node is None:
            return "-"
        if node.left is None and node.right is None:
            return str(node.value)
        return "(" + self._recursivePrint(node.left) + " " + str(node.value) + " " + self._recursivePrint(node.right) + ")"
        
