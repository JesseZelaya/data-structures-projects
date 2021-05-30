# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jesse Zelaya
# Description: Heap assignment


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
            Adds to the heap and percolates upward if less than parent
        """
        if self.is_empty():
            self.heap.append(node)
        else:
            # insert value into next empty array
            self.heap.append(node)

            # get index where node was placed
            node_index = self.heap.length() - 1

            # percolate upward
            self.percolate_up(node_index)

    def percolate_up(self, node_index):
        """
            Compares node leaf or child node with parent and swaps
            as necessary. Travels upward toward root of heap.
        """
        new_node = self.heap.get_at_index(node_index)
        parent_index = (node_index - 1) // 2

        # compare child to parent and swap if parent is greater
        # do until parent is 0

        parent = self.heap.get_at_index(parent_index)

        # root_bool checks to see if it has reached the root node
        root_bool = False
        while root_bool is False:
            if parent_index == 0:
                root_bool = True
            # if the parent violates min heap structure, then swap
            if parent > new_node:
                self.heap.swap(node_index, parent_index)
                node_index = parent_index
                parent_index = (node_index-1) // 2
                parent = self.heap.get_at_index(parent_index)
                new_node = self.heap.get_at_index(node_index)
            else:
                break

    def percolate_down(self, main_index):
        """
            percolates/bubbles downward away from node and to the lowest position on the heap
        """
        main_node = self.heap.get_at_index(main_index)

        # compare to children and percolate downward
        left_index = (2*main_index) + 1
        right_index = (2*main_index) + 2
        length = self.heap.length()
        track_min = None
        end_bool = False

        # check until end bool is true and main_index is less than total length
        while main_index < length and end_bool is False:
            # tracks minimum index of children
            track_min = None

            # check left index, vs main node
            if left_index < length and self.heap.get_at_index(left_index) < main_node:
                track_min = left_index

            # check right index vs main node and double check that it only updates if
            # the right index value is lower than the left index value
            if right_index < length and self.heap.get_at_index(right_index) < main_node:
                if self.heap.get_at_index(left_index) > self.heap.get_at_index(right_index):
                    track_min = right_index

            # assure both indices are within range and check for equal index location values
            if left_index < length and right_index < length:
                if self.heap.get_at_index(left_index) == self.heap.get_at_index(right_index):
                    if self.heap.get_at_index(main_index) > self.heap.get_at_index(left_index):
                        track_min = left_index

            # if nothing was updated then track min is still none so switch endbool to true to break loop
            if track_min is not None:
                self.heap.swap(main_index, track_min)
                main_index = track_min
            else:
                end_bool = True

            # update indices
            left_index = (2*main_index) + 1
            right_index = (2*main_index) + 2

    def get_min(self) -> object:
        """
            This method returns an object with a minimum key without removing it from the heap. If
            the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
            This method returns an object with a minimum key and removes it from the heap. If the
            heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException
        elif self.heap.length() == 1:
            return self.heap.pop()
        else:
            # swap values and pop min then percolate down
            self.heap.swap(0, self.heap.length()-1)
            min_value = self.heap.pop()
            self.percolate_down(0)
            return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
            Builds heap given an array
        """
        # clear heap by replacing with given array
        new_arr = DynamicArray()
        length = da.length()

        for i in range(0,length):
            new_arr.append(da.get_at_index(i))

        self.heap = new_arr
        # find starting point to build heap
        start_index = (da.length() - 1)//2

        # decrement down to root to percolate down from that point
        for i in range(start_index, -1, -1):
            self.percolate_down(i)



# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print('----my get min test----')
    m = MinHeap()
    print(h)
    print(h.get_min(), h.get_min())


    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    # h = MinHeap([2,3,4,5,6,8,9,10,7])
    # print(h, end=' ')
    # print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)

    print('------build heap---------')
    da = DynamicArray([5,2,11,8,6,20,1,3,7])
    m = MinHeap(['zebra', 'apple'])
    print(m)
    m.build_heap(da)
    print(m)

