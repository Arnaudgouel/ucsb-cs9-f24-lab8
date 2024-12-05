import sys
from skew import SkewMinHeap

heap = SkewMinHeap()
def main():
    for line in sys.stdin:
        handleInput(line)

def handleInput(line):
    line = line.strip().split()
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
    heap.count()

def popHeapTree():
    heap.pop()

def printHeapTree():
    heap.print()

def pushIntoHeapTree(line):
    if len(line) == 1:
        print("ERROR: No argument.")
    line = " ".join(line[1:])
    heap.push(line)

def topHeapTree():
    heap.top()

def handleEmptyHeapTree():
    print("ERROR: Heap is empty.")

main()