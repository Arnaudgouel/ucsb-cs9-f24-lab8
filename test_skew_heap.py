import unittest
from io import StringIO
import sys
from skew import SkewMinHeap

class TestSkewHeap(unittest.TestCase):
    def setUp(self):
        """Create a fresh heap before each test"""
        self.heap = SkewMinHeap()
        # Set up string capture for testing printed output
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore normal stdout after each test"""
        sys.stdout = sys.__stdout__

    def get_output(self):
        """Helper to get the captured output"""
        return self.held_output.getvalue().strip()

    def test_empty_heap_operations(self):
        """Test operations on an empty heap"""
        # Test count on empty heap
        self.assertEqual(self.heap.count(), 0)
        
        # Test pop on empty heap
        self.assertEqual(self.heap.pop(), "ERROR: Heap is empty.")
        
        # Test top on empty heap
        
        self.assertEqual(self.heap.top(), "ERROR: Heap is empty.")
        
        # Test print on empty heap
        self.heap.print()
        self.assertEqual(self.get_output(), "ERROR: Heap is empty.")

    def test_push_single_element(self):
        """Test pushing a single element"""
        self.heap.push("A")
        self.assertEqual(self.heap.count(), 1)
        self.heap.print()
        self.assertEqual(self.get_output(), "A")

    def test_push_multiple_elements(self):
        """Test pushing multiple elements"""
        elements = ["B", "A", "C"]
        for elem in elements:
            self.heap.push(elem)
        
        self.assertEqual(self.heap.count(), 3)
        self.heap.print()
        # The exact structure might vary but 'A' should be at the root
        self.assertEqual(self.heap.top(), "A")

    def test_push_with_spaces(self):
        """Test pushing strings containing spaces"""
        self.heap.push("Hello World")
        self.heap.push("A B C")
        self.assertEqual(self.heap.count(), 2)
        # "A B C" should be root as it comes first alphabetically
        self.assertEqual(self.heap.top(), "A B C")

    # def test_push_empty_string(self):
    #     """Test pushing empty string"""
    #     self.heap.push("")
    #     self.assertEqual(self.get_output(), "ERROR: No argument.")
    #     self.assertEqual(self.heap.count(), 0)

    def test_pop_order(self):
        """Test that elements are popped in ascending order"""
        elements = ["C", "A", "B", "D"]
        for elem in elements:
            self.heap.push(elem)
        
        popped = []
        for _ in range(len(elements)):
            popped.append(self.heap.pop())
        
        self.assertEqual(popped, sorted(elements))

    # def test_merge_functionality(self):
    #     """Test the merge operation"""
    #     # Create two heaps
    #     heap1 = SkewMinHeap()
    #     heap2 = SkewMinHeap()
        
    #     # Add elements to first heap
    #     heap1.push("B")
    #     heap1.push("D")
        
    #     # Add elements to second heap
    #     heap2.push("A")
    #     heap2.push("C")
        
    #     # Merge heaps
    #     merged_root = heap1.merge(heap1.root, heap2.root)
    #     heap1.root = merged_root
        
    #     # Test the merged heap properties
    #     self.assertEqual(heap1.top(), "A")
    #     popped = []
    #     while heap1.count() > 0:
    #         popped.append(heap1.pop())
    #     self.assertEqual(popped, ["A", "B", "C", "D"])

    def test_complex_operations(self):
        """Test a complex sequence of operations"""
        heap = SkewMinHeap()

        operations = [
            ("push", "M"),
            ("push", "F"),
            ("push", "Z"),
            ("pop", None),
            ("push", "A"),
            ("push", "Q"),
            ("pop", None),
            ("top", None)
        ]
        
        expected_sequence = ["F", "A"]  # Expected pop results
        i = 0
        for op, value in operations:
            if op == "push":
                heap.push(value)
            elif op == "pop":
                result = heap.pop()
                if result is not None:
                    self.assertEqual(result, expected_sequence.pop(0))
                    i += 1
            elif op == "top":
                self.assertEqual(heap.top(), "M")

    # def test_ascii_ordering(self):
    #     heap = SkewMinHeap()
    #     heap.print()
    #     """Test that strings are ordered by ASCII values"""
    #     elements = ["a", "A", "b", "B", "1", "2", " "]
    #     for elem in elements:
    #         heap.push(elem)
        
    #     popped = []
    #     while heap.count() > 0:
    #         popped.append(heap.pop())
        
    #     self.assertEqual(popped, sorted(elements))

    def test_gradescope(self):
        """Test the example from the Gradescope test case"""
        heap = SkewMinHeap()
        heap.push("A")
        heap.push("B")
        heap.push("C")
        
        self.assertEqual(heap.count(), 3)
        self.assertEqual(heap.top(), "A")
        heap.print()
        self.assertEqual(self.get_output(), "(A B C)")

        popped = []
        for _ in range(3):
            popped.append(heap.pop())
        
        self.assertEqual(popped, ["A", "B", "C"])

if __name__ == '__main__':
    unittest.main()