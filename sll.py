# Course: CS261 - Data Structures
# Student Name: Jesse Zelaya
# Assignment: Single linked list
# Description: create a single linked list



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds value as a new node to the front of the LL after the head
        """

        cur = self.head
        newLink = SLNode(value)
        newLink.next = cur.next
        cur.next = newLink

    def add_back(self, value: object) -> None:
        """
        Adds value as a new node to the back of the LL before the tail
        """
        # traverse the list to find last node
        # create new node for value, and adjust pointers as needed
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next

        newLink = SLNode(value)
        newLink.next = cur.next
        cur.next = newLink

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts at a given index in the LL
        Raises exception for invalid indices
        """
        if index < 0 or index > self.length():
            raise SLLException

        cur = self.head
        for i in range(index):
            cur = cur.next

        # create new link and insert
        newLink = SLNode(value)
        newLink.next = cur.next
        cur.next = newLink

    def remove_front(self) -> None:
        """
            removes front link
        """
        if self.length() == 0:
            raise SLLException

        # point cur next to skip the next link
        cur = self.head
        cur.next = cur.next.next

    def remove_back(self) -> None:
        """
            removes back link
        """
        if self.length() == 0:
            raise SLLException

        cur = self.head

        while cur.next.next != self.tail:
            cur = cur.next

        # remove link
        cur.next = cur.next.next

    def remove_at_index(self, index: int) -> None:
        """
            removes link at given index
        """
        if index < 0 or index > self.length() - 1:
            raise SLLException

        cur = self.head

        # find the position prior to the index
        # point current to the position ahead of the next
        for i in range(0, index):
            cur = cur.next

        cur.next = cur.next.next

    def get_front(self) -> object:
        """
            get value at front of list
        """
        if self.length() == 0:
            raise SLLException

        cur = self.head
        return cur.next.value

    def get_back(self) -> object:
        """
            get value at back of list
        """
        if self.length() == 0:
            raise SLLException

        cur = self.head

        while cur.next != self.tail:
            cur = cur.next

        return cur.value

    def remove(self, value: object) -> bool:
        """
            remove link with given value
        """

        cur = self.head

        while cur.next.value != value and cur.next != self.tail:
            cur = cur.next

        if cur.next == self.tail:
            return False
        else:
            cur.next = cur.next.next

            return True

    def count(self, value: object) -> int:
        """
            count links with given value
            return count
        """
        cur = self.head
        count = 0
        length = self.length()

        for i in range(0, length+1):
            if cur.value == value:
                count +=1
            cur = cur.next

        return count

    def slice(self, start_index: int, size: int) -> object:
        """
            takes a slice of list and puts in new SLL
        """
        newLL = LinkedList()
        length = self.length()
        # given exceptions
        if size < 0 or start_index >= length:
            raise SLLException
        if start_index < 0 or length < (size - start_index) or size > (length-start_index):
            raise SLLException

        cur = self.head
        newcur = newLL.head

        # iterate and copy links in given range
        for i in range(0, start_index + size):
            cur = cur.next
            if i >= start_index:
                val = cur.value
                newLink = SLNode(val)
                newLink.next = newcur.next
                newcur.next = newLink
                newcur = newcur.next

        return newLL








if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)

    #
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 1, 2, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))

    #
    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    # print('\n# slice example 2')
    # list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")
    #
