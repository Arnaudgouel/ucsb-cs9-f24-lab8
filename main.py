import sys
from skew import SkewMinHeap

heap = SkewMinHeap()
def main():
    for line in sys.stdin:
        handleInput(line)

def handleInput(line):
    line = line.strip().split(" ", maxsplit=1)
    if len(line) == 0:
        return
    firstArgument = line[0]
    if firstArgument == "count":
        countHeapTree()
    elif firstArgument == "pop":
        popHeapTree()
    elif firstArgument == "print":
        printHeapTree()
    elif firstArgument == "push":
        pushIntoHeapTree(line)
    elif firstArgument == "top":
        topHeapTree()
    else:
        return

def countHeapTree():
    print(heap.count())

def popHeapTree():
    print(heap.pop())

def printHeapTree():
    heap.print()

def pushIntoHeapTree(line):
    if len(line) == 1:
        print("ERROR: No argument.")
        return
    line = line[1].strip()
    heap.push(line)

def topHeapTree():
    print(heap.top())

def handleEmptyHeapTree():
    print("ERROR: Heap is empty.")
if __name__ == "__main__":
    main()