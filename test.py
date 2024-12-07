from skew import SkewMinHeap

# Simple test to debug
heap = SkewMinHeap()
heap.push("A")
heap.push("B")
heap.push("C")
heap.push("D")
heap.push("E")

print("Count:", heap.count())  # Should be 3
print("Top value:", heap.top())  # Should be "A"
print("Tree structure:")
heap.print()  # Should show the tree

# Pop all values to check order
print("\nPopping all values:")
while heap.count() > 0:
    print(heap.pop())  # Should print A, B, C in order