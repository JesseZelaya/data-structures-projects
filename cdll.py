# Course: CS261 - Data Structures
# Student Name: Jesse Zelaya
# Assignment: Double linked list
# Description:  my very own double linked list with functions


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        creates node with value given and adds to front
        """
        # set cur to sentinel
        cur = self.sentinel

        # create new node
        newLink = DLNode(value)

        # insert new node
        newLink.next = cur.next
        newLink.prev = cur.next.prev
        cur.next.prev = newLink
        cur.next = newLink

    def add_back(self, value: object) -> None:
        """
            creates new node from value and adds it to the back
        """
        # set cur to sentinel
        cur = self.sentinel

        # new link with value
        newLink = DLNode(value)

        # set current to the previous (end of circular)
        cur = cur.prev
        # set the previous of current next to newLink
        cur.next.prev = newLink
        #set newlink next to current's next
        newLink.next = cur.next
        # set newlink's previous to current
        newLink.prev = cur
        # set current next to new link
        cur.next = newLink

    def insert_at_index(self, index: int, value: object) -> None:
        """
            inserts node with value given at given index
        """
        length = self.length()
        if index < 0 or (index > length and index > 0 ):
            raise CDLLException

        # case for index in first half of list
        if index <= length/2:
            cur = self.sentinel

            newLink = DLNode(value)
            for i in range(0, index):
                cur = cur.next
            #insert node new link at current spot (at index)
            newLink.next = cur.next
            newLink.prev = cur.next.prev
            cur.next.prev = newLink
            cur.next = newLink
        # case for back half
        else:

            cur = self.sentinel
            newLink = DLNode(value)

            #insert node new link at current spot (at index)
            for i in range(length, index -1, -1):
                cur = cur.prev
            newLink.next = cur.next
            newLink.prev = cur.next.prev
            cur.next.prev = newLink
            cur.next = newLink

    def remove_front(self) -> None:
        """
            remove first node
        """
        if self.is_empty():
            raise CDLLException

        cur = self.sentinel

        # remove node
        cur.next.next.prev = cur
        cur.next = cur.next.next

    def remove_back(self) -> None:
        """
            remove back node
        """
        if self.is_empty():
            raise CDLLException
        cur = self.sentinel

        # remove node
        cur.prev.prev.next = cur
        cur.prev = cur.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
            Removes node at index given
        """
        length = self.length()
        if self.is_empty() or index < 0 or index > length - 1:
            raise CDLLException

        # case for index in first half of list
        if index <= length / 2:
            cur = self.sentinel

            #remove node
            for i in range(0, index):
                cur = cur.next
            cur.next.next.prev = cur
            cur.next = cur.next.next

        # case for back half iteration
        else:
            cur = self.sentinel
            # remove node
            for i in range(length, index - 1, -1):
                cur = cur.prev
            cur.next.next.prev = cur
            cur.next = cur.next.next

    def get_front(self) -> object:
        """
        returns value at front of LL
        """
        if self.is_empty():
            raise CDLLException

        cur = self.sentinel
        return cur.next.value

    def get_back(self) -> object:
        """
            returns value at back of list
        """
        if self.is_empty():
            raise CDLLException
        cur = self.sentinel
        return cur.prev.value


    def remove(self, value: object) -> bool:
        """
            removes first instance of value given
        """
        cur = self.sentinel

        # iterate and remove node with given value
        while cur.next.value != value and cur.next != self.sentinel:
            cur = cur.next

        if cur.next.value == value:
            cur.next.next.prev = cur
            cur.next = cur.next.next
            return True
        return False

    def count(self, value: object) -> int:
        """
            counts all links with given value
        """
        cur = self.sentinel
        count = 0

        while cur.next != self.sentinel:
            if cur.next.value == value:
                count += 1
            cur = cur.next

        return count

    def adjacent_swap(self, cur_first, cur_second):
        """swaps adjacent indices"""
        # saves current next nodes for returning in certain cases
        c1,c2 = cur_first.next, cur_second.next.next

        cur_second.next, cur_first.next = cur_first, cur_second.next
        cur_second.prev, cur_first.prev = cur_first.prev, cur_second
        cur_second.prev.next, cur_first.next.prev = cur_second, cur_first

        return c1,c2


    def local_swap(self, cur_1, cur_2):
        """
            swaps non adjacent values in linked list
            takes nodes at index swap positions
        """
        # save temps for cur1, cur 2
        cur_1_save, cur_2_save = cur_1.next, cur_2.prev

        cur_1.prev, cur_2.prev = cur_2.prev, cur_1.prev
        cur_1.prev.next, cur_2.prev.next = cur_1, cur_2

        cur_1.next, cur_2.next = cur_2.next, cur_1.next
        cur_1.next.prev, cur_2.next.prev = cur_1, cur_2



        return cur_1_save, cur_2_save

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
            swaps at two given indices
        """
        length = self.length()

        # check for valid index
        if index1 < 0 or index1 > (length-1):
            raise CDLLException
        if index2 < 0 or index2 >(length-1):
            raise CDLLException

        # if indices are the same return None and don't change anything
        if index2 == index1:
            pass
        else:
            # create currents for both indices
            cur_1 = self.sentinel  # index 1
            cur_2 = self.sentinel  # index 2

            # go to the position for the index nodes
            for i in range(0, index1+1):
                cur_1 = cur_1.next

            # position for index 2
            for i in range(0, index2+1):
                cur_2 = cur_2.next

            # for adjacent values
            if index2 < index1 and abs(index1-index2) == 1:
                self.adjacent_swap(cur_2, cur_1)
            elif index2 > index1 and abs(index1 - index2) == 1:
                self.adjacent_swap(cur_1, cur_2)

            else:
                self.local_swap(cur_1, cur_2)

    def reverse(self) -> None:
        """
            reverses list
        """
        cur_1 = self.sentinel
        cur_2 = self.sentinel
        length = self.length()
        # reverse for even and odd
        if length == 2:
            self.adjacent_swap(cur_1.next, cur_2.prev)

        # for even lists you need to swap middle values (adjacent)
        elif length % 2 == 0:
            cur_1 = cur_1.next
            cur_2 = cur_2.prev
            min_flag = 0
            for i in range(0, (length//2) - 2):
                min_flag = 1
                cur_1, cur_2 = self.local_swap(cur_1, cur_2)
            cur_1, cur_2 = self.local_swap(cur_1, cur_2)
            if cur_2.value != cur_1.value:
                self.adjacent_swap(cur_1, cur_2)

        else:
            cur_1 = cur_1.next
            cur_2 = cur_2.prev
            for i in range(0, (length//2)):

                cur_1, cur_2 = self.local_swap(cur_1, cur_2)

    def sort(self) -> None:
        """
            sorts in ascending order
        """
        ll_length = self.length()
        swap_flag = True

        # goes through bubble sort until no swaps are done
        while swap_flag:
            swap_flag = False
            cur = self.sentinel.next
            while cur.next.value is not None and cur.value is not None:
                if cur.value > cur.next.value:
                    self.adjacent_swap(cur, cur.next)
                    swap_flag = True
                cur = cur.next

    def rotate(self, steps: int) -> None:
        """
            rotates in negative and positive directions
        """
        cur = self.sentinel
        length = self.length()
        # cases for length 0, if steps mod are == 0, and final
        if length == 0:
            pass
        elif ((-1)*steps)%length == 0:
            pass
        else:
            steps = ((-1) * steps) % length
            count = 0
            while (count < steps):
                cur = cur.next
                count += 1

            # remove sentinel
            self.sentinel.prev.next = self.sentinel.next
            self.sentinel.next.prev = self.sentinel.prev

            # replace sentinel at step position
            self.sentinel.next = cur.next
            self.sentinel.prev = cur.next.prev
            cur.next.prev = self.sentinel
            cur.next = self.sentinel

    def remove_duplicates(self) -> None:
        """
            removes all instances of nodes that had duplicate values
        """
        cur = self.sentinel
        trip_flag = True
        value_removed = None

        # goes through list and keeps track of next value before removals with trip_flag
        # checks current with value_removed to see if it is part of a duplicate family
        while cur.next.value is not None and cur is not None:
            if trip_flag is not True:
                temp = cur.next
                trip_flag = True
            else:
                temp = cur.next
            if cur.next.value == cur.value:
                trip_flag = False
                value_removed = cur.value
                cur.next.prev, cur.prev.next = cur.prev, cur.next

            #update to next node
            cur = temp

            # if trip_flag is false and value removed is the same, remove current node
            if trip_flag is False and value_removed == cur.value:
                cur1 = cur.prev
                cur1.next.next.prev = cur1
                cur1.next = cur1.next.next

    def odd_even(self) -> None:
        """
            sends even indices to back of list
            eg [a,s,d,f] gives [a,d,s,f]
        """
        cur = self.sentinel.next
        count = 1
        length = self.length()
        # add 1 to length because you want the full range of link nodes
        while count < length+1:
            cur_temp = cur.next

            if count%2 == 0 and cur.next is not None:
                temp = cur

                cur.next.prev, cur.prev.next = cur.prev, cur.next

                # set current to the previous (end of circular)
                remove_current = self.sentinel.prev
                # set the previous of current next to newLink
                remove_current.next.prev = temp
                # set newlink next to current's next
                temp.next = remove_current.next
                # set newlink's previous to current
                temp.prev = remove_current
                # set current next to new link
                remove_current.next = temp

            cur = cur_temp
            count +=1


if __name__ == '__main__':
    pass


    #
    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)

    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)
    #
    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'),(3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst, "length", lst.length())
    #
    #     except Exception as e:
    #         print(type(e))
    #
    # lst2 = CircularList()
    # lst2.add_front('a')
    # lst2.add_front('x')
    # lst2.add_front('m')
    # lst2.add_front('k')
    #
    #
    #
    # print(lst2, lst2.length())
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)
    #
    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)

    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))

    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())
    #
    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3, 1]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))


    # self test swap
    # lst = CircularList([6,5,4,3,2,1,0])
    # print(lst)
    # print("swap nodes ", 0,6, ' ' )
    # lst.swap_pairs(1,2)
    # print(lst)


    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6,7,8,9,10])
    # # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    # #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # # test_cases = [(0, 11), (0, 10), (11, 0), (10, 0), (0, 1), (1, 0),
    # #               (10, 9), (9, 10), (3, 5), (3, 4), (7, 6), (0, 0)]
    # test_cases = [(0, 11), (0, 10), (10, 0), (3,5),(3,9),(10, 0), (0, 1), (1, 0),
    #               (10, 9), (9, 10), (3, 5), (3, 1), (6, 8), (0, 0)]
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    # lst.swap_pairs(1,2)
    # print("doneeeee", lst)
    #
    # lst.swap_pairs(0, 1)
    # print("doneeeee", lst)
    #
    # lst.swap_pairs(1, 0)
    # print("doneeeee", lst)

    #
    # print('\n# reverse example 1')
    # test_cases = (
    #     [1, 2, 3, 3, 4, 5],
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)

    # print('\n# reverse example 1')
    # test_cases = (
    #
    #     [1, 2, 3, 4, 5],
    #     ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)

    # print('\n# reverse example 2')
    # lst = CircularList()
    # print(lst)
    # lst.reverse()
    # print(lst)
    # lst.add_back(2)
    # lst.add_back(3)
    # lst.add_front(1)
    # lst.reverse()
    # print(lst)

    # print('\n# reverse example 3')
    #
    #
    # class Student:
    #     def __init__(self, name, age):
    #         self.name, self.age = name, age
    #
    #     def __eq__(self, other):
    #         return self.age == other.age
    #
    #     def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)
    #
    #
    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)
    #
    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)
    #
    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)

    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # lst = CircularList(source)
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst.rotate(steps)
    #     print(lst)
    #
    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)

    # lst = CircularList([10, 20, 30, 40])
    # print(lst)
    # lst.rotate(-3)
    # print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)

    print('\n# remove_duplicates example 1')
    # test_cases = (
    # [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    # [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    # [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],list("abccd"),list("005BCDDEEFI")
    # )

    # test_cases = (
    #     [1, 2, 3, 4, 5], [1, 1, 1, 1, 1], [], [1], [1, 1], [1, 1, 1, 2, 2, 2], [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
    #     list("abccd"),
    #     list("005BCDDEEFI")
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)

    #print(list("032hfsha"))
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)
    #
    print('\n# odd_even example 1')
    # test_cases = (
    # [1, 2, 3, 4, 5], list('ABCDE'),
    # [], [100], [100, 200], [100, 200, 300],
    # [100, 200, 300, 400],
    # [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E'] )


    lst = CircularList([10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E'])
    print('INPUT :', lst)
    lst.odd_even()
    print('OUTPUT:', lst)
