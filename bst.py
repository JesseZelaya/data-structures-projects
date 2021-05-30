# Course: CS261 - Data Structures
# Student Name: Jesse Zelaya
# Assignment: Tree Search
# Description: Implements a search tree using Stacks and Queue


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
            adds tree node with a value given to the current tree
        """
        # make new node
        new_node = TreeNode(value)



        if self.root is None:
            self.root = new_node

        else:
            current = self.root
            current_last = None
            while current is not None:
                # keep your place for when the loop breaks
                current_last = current
                if current.value == value:
                    current = current.right
                elif current.value > value:
                    current = current.left
                elif current.value < value:
                    current = current.right

            # once out of the loop check to see if
            # its equal or less than the given value
            # if it's equal you must put it on the right
            # if it's less then it also goes on the right, else left
            if current_last.value == value or current_last.value < value:
                current_last.right = new_node
            elif current_last.value > value:
                current_last.left = new_node


    def contains(self, value: object) -> bool:
        """
            This method returns True if the value parameter is in the BinaryTree or False if it is not in
            the tree. If the tree is empty, the method should return False.
        """
        if self.root is None:
            return False
        else:
            current = self.root

            while current is not None:
                if value == current.value:
                    return True
                elif current.value > value:
                    current = current.left
                elif current.value < value:
                    current = current.right
            return False

    def get_first(self) -> object:
        """
            This method returns the value stored at the root node. If the BinaryTree is empty, this
            method returns None.
        """
        return self.root.value

    def remove_first(self) -> bool:
        """
            This method must remove the root node in the BinaryTree. The method must return False if
            the tree is empty and there is no root node to remove and True if the root is removed.
        """
        if self.root is None:
            return False

        else:
            parent_node = self.root
            successor = parent_node.right

            # if no successor to the right
            if successor is None:
                self.root = parent_node.left
            else:
                # find right child's most left successor
                parent_successor = None
                while successor.left is not None:
                    parent_successor = successor
                    successor = successor.left

                if parent_successor is None:
                    successor.left = self.root.left
                    #successor.right = self.root.right

                else:
                    parent_successor.left = successor.right

                    successor.left = parent_node.left
                    successor.right = parent_node.right
                    pass


                self.root = successor
                return True



            return True

    def remove(self, value) -> bool:
        """
            This method should remove the first instance of the object in the BinaryTree. The method
            must return True if the value is removed from the BinaryTree and otherwise return False.
        """
        if self.root is None:
            return False
        elif self.root.value == value:
            return self.remove_first()
        # check if value is in tree
        elif self.contains(value) is False:
            return False

        # having checked if these conditions are met check to see if I can
        # find the node and parent

        # find node and parent node
        parent_node = None
        node = self.root
        parent_successor = None
        #successor = None
        child_left = False
        child_right = False

        while node is not None and node.value != value:
            parent_node = node
            if node.value >value:
                node = node.left
                child_left = True
                child_right = False
            elif node.value < value:
                node = node.right
                child_right = True
                child_left = False

        # with the node found check to see if there is a right value
        if node.right is None:
            if child_right:

                parent_node.right = node.left
                #parent_node.left = node.right
                return True
            elif child_left:
                parent_node.left = node.left
                #parent_node.right = node.right
            return True

        # if node has a right, but no right.left successor
        # if parent successor == successor

        elif node.right.left == None:
            #print("ELSH IF WORKED")

            successor = node.right

            # print(parent_successor)
            # print(successor)

            successor.left = node.left

            # direct which branch is being adjusted
            if child_left:
                parent_node.left = successor
            elif child_right:
                parent_node.right = successor
            return True
        else:
            #print("final")
            successor = node.right
            while successor.left is not None:
                parent_successor = successor
                successor = successor.left

            if parent_successor is None:
                parent_node.right = successor
                successor.left = node.left
                #successor.left = node.left
                # successor.left = parent_node.left
                # successor.right = current.right
                return True
            else:
                parent_successor.left = successor.right
                if child_right:
                    parent_node.right, successor.right = successor, node.right
                    successor.left = node.left
                elif child_left:
                    parent_node.left, successor.right = successor, node.right
                    successor.left = node.left
                return True

    def pre_order_traversal(self) -> Queue:
        """
            Returns a q with a pre order traversal of BST. Each parent followed by child left and right
        """

        # save node to follow and queue
        node = self.root
        q_travel = Queue()

        #check if empty
        if self.root is None:
            return q_travel

        #--- following implemented in helper function---
        # start with left side of tree
        # then with right side of tree
        # call function to push children onto q
        # go to next node

        self.pre_order_traversal_help(q_travel, node)
        return q_travel

    def pre_order_traversal_help(self, q, node):
        """
            pushes values on to the q while loop traverses
        :param q: q with order of values
        :param node: given node
        :return: nothing
        """
        q.enqueue(node)

        # check left and right sides of tree for each node
        if node.left is not None:
            self.pre_order_traversal_help(q, node.left)

        if node.right is not None:
            self.pre_order_traversal_help(q, node.right)


    def in_order_traversal(self) -> Queue:
        """
            returns a q with in order q of tree nodes
        """
        # save node to follow and create q
        node = self.root
        q_travel = Queue()

        # check root
        if node is None:
            return q_travel

        self.in_order_traversal_help(q_travel, node)
        return q_travel

    def in_order_traversal_help(self, q_travel, node, p_node = None):
        """
            helper function for in order traversal
        """
        # q_travel.enqueue(node)

        # check left and right sides of tree for each node
        # this is slighty different from pre order
        # this travels left until the next left is None and it skips the call and then pushes that
        # value onto queue

        
        if node.left is not None:
            self.in_order_traversal_help(q_travel, node.left)

        # position of enqueue enqueues the parent of the child nodes AFTER the end is reached
        q_travel.enqueue(node)

        if node.right is not None:
            self.in_order_traversal_help(q_travel, node.right)


    def post_order_traversal(self) -> Queue:
        """
            returns q of list that is in post order, with children before parent nodes
        """
        # save node to follow and create q
        node = self.root
        q_travel = Queue()

        # check root
        if node is None:
            return q_travel

        self.post_order_traversal_help(q_travel, node)
        return q_travel


    def post_order_traversal_help(self, q_travel, node):
        """
            helper function for post order traversal
        :param q_travel: current queue
        :param node: current node
        :return: None
        """

        if node.left is not None:
            self.post_order_traversal_help(q_travel, node.left)

        if node.right is not None:
            self.post_order_traversal_help(q_travel, node.right)

        # node is added at the end of the helper function
        # this assures we're at the bottom most node
        q_travel.enqueue(node)

    def by_level_traversal(self) -> Queue:
        """
            Returns q with by level traversal of tree
        """
        # check if empty and create node
        q_travel = Queue()
        node = self.root
        temp_q = Queue()


        if node is None:
            return q_travel

        #while current node is not None
        temp_q.enqueue(node)

        # keep temporary queue as a place holder
        # while temp is empty stay in loop
        # update node as you go
        # i have to keep the None types in and update as I go
        # as i dequeue it gets rid of the nones.
        while temp_q.is_empty() is False:
            node = temp_q.dequeue()

            if node is not None:
                q_travel.enqueue(node)

                temp_q.enqueue(node.left)
                temp_q.enqueue(node.right)


        return q_travel

    def my_complete(self):
        """my complete check"""

        if self.root is None:
            return True
        if self.is_complete():
            return True

        q = Queue()

        node = self.root
        q.enqueue(node)

        while q.is_empty() is False:
            node = q.dequeue()

            if node is not None:
                if node.left is None and node.right is None:
                    return True
                else:
                    return False
    def is_full(self) -> bool:
        """
            checks to see if each parent has two children
        """
        # set node as root and check if empty
        node = self.root
        q_full = Queue()
        if self.root is None:
            return True

        if (self.root.left is None and self.root.right is not None \
                or self.root.left is not None and self.root.right is None):
            return False
        self.is_full_help(node, q_full)

        tree_size = self.size()
        is_full = True
        for i in range(tree_size):
            node = q_full.dequeue()
            if (node.left is not None and node.right is None) or (node.left is None and node.right is not None):
                is_full = False

        return is_full

    def is_full_help(self, node, q):
        """
            helps is full method
        """
        # traverse through nodes and check for child left and right
        if node.left is not None:
            self.is_full_help(node.left, q)

        q.enqueue(node)

        if node.right is not None:
            self.is_full_help(node.right,q)

    def is_complete(self) -> bool:
        """
            checks if binary search tree is complete:
            I tried. :'(. ran out of time
        """
        # travel laterally until you find a parent with no child

        # if self.root is None:
        #     return True
        # if self.root.left is None and self.root.right is None:
        #     return True
        if self.is_perfect():
            return True

        # create q
        q_travel = Queue()

        # create node
        node = self.root

        # create temp q
        q_temp = Queue()

        # while temp is not empty continue
        # if not none process
        # search for node without leaf
        q_temp.enqueue(node)

        node_count = self.my_count()

        return self.is_complete_help(node, 0, node_count)


    def is_complete_help(self, node, index, node_count):

        if node is None:
            return True

        if index >= node_count:
            return False

        return (self.is_complete_help(node.left, 2*index+1, node_count)
                and self.is_complete_help(node.right, 2*index+2, node_count))


    def my_count(self):
        """ redone count"""
        return self.my_count_help(self.root)

    def my_count_help(self, node):
        """helper for redone count"""
        if node is None:
            return 0
        return 1 + self.my_count_help(node.left) + self.my_count_help(node.right)

    def is_perfect(self) -> bool:
        """
            returns true or false if tree is perfect
        """
        node = self.root

        if node is None or (node.left is None and node.right is None):
            return True
        # get height use formula to check if perfect
        height = self.height()

        leaves = self.size()

        height_to_leaves = 2**(height + 1) -1

        if height_to_leaves == leaves:
            return True
        else:
            return False

    def is_perfect_help(self, node):
        """ is perfect helper"""
        pass

    def size(self) -> int:
        """
            returns the number of nodes in a tree
        """

        node = self.root
        stack = Stack()
        stack.push(node)

        # goes through each node and pushes onto a stack
        # the stack can be popped and counted afterward
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        self.size_help(node,stack)

        stack_count = 0
        while stack.is_empty() is False:
            stack_count += 1
            stack.pop()
        return stack_count -1

    def size_help(self, node, stack):

        stack.push(node)

        if node.left is not None:
            self.size_help(node.left, stack)

        if node.right is not None:
            self.size_help(node.right, stack)

    def height(self) -> int:
        """
            gets the height of tree
        """
        node = self.root
        return self.height_help(node)

    def height_help(self, node):
        """ helper function for height"""
        if node is None:
            return -1

        # find max for left and right
        left = self.height_help(node.left)
        right = self.height_help(node.right)

        return max(left, right)+1

    def count_leaves(self) -> int:
        """
            Uses is full helper to get queue of nodes and checks for nodes with no children
        """
        node = self.root
        q_leave = Queue()

        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1


        # get queue from helper
        self.is_full_help(node, q_leave)

        leaves_size = self.size()
        leaf_count = 0

        for i in range(leaves_size):
            node = q_leave.dequeue()
            if node.left is None and node.right is None:
                leaf_count += 1


        return leaf_count

    def count_unique(self) -> int:
        """
            counts unique values in tree
        """

        node = self.root
        stack = Stack()
        unique_count = 0

        if self.root is None:
            return 0
        if node.left is None and node.right is None:
            return 1

        # start a place holder for stack for use in while loop
        stack.push(None)
        self.count_unique_help(node, stack)

        while stack.top() is not None:
            value = stack.pop()
           # temp_val = stack.pop()
            if value != stack.top():#and stack.is_empty() is False:
                unique_count += 1
            # else:
            #     stack.pop()
            #     unique_count += 1

        return unique_count

    def count_unique_help(self, node, stack):

        if node.left is not None:
            self.count_unique_help(node.left, stack)

        # ordered stack
        stack.push(node.value)

        if node.right is not None:
            self.count_unique_help(node.right, stack)


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':

    tree = BST([1,2,3,4,5])
    print(tree.my_count())
    # #-------test is full-----------
    # tree = BST([10, 5])
    # tree9 = BST([97256, -24847])
    # print(tree.is_complete(), 'true')
    # print(tree9.is_complete(), 'true')

    # """ add() example #1 """
    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)
    #
    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    #
    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))
    #
    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))
    #
    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)
    #
    # """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))
    #
    # """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(20))
    # print(tree)
    # #
    # """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree)
    # print(tree.remove(20))
    # print(tree)
    #
    #
    #
    # print("--------------STRING CASE-----------------")
    # tree = BST(['F', 'E', 'JI', 'HK', 'F', 'LM'])
    # print(tree)
    # print(tree.remove('HK'))
    # print(tree)
    #
    # print("-------------------------------")
    # tree = BST([1,2,2,3,3,3])
    # print(tree)
    # print(tree.remove(2))
    # print(tree)
    # #
    # print("------------------Self test 2 remove-------------")
    # tree = BST([0, -2, -3, -4, -10, 3, 2, 2, 9])
    # print(tree)
    # print(tree.remove(3))
    # #print(tree)
    #
    # print("------------------Self test 3 remove-------------")
    # tree = BST([-5, -10, 7, 4, 3, 2, 6, 7, 10])
    # print(tree)
    # print(tree.remove(2))
    # print(tree)
    #
    #
    # print("----------Self test 4 remove---------")
    #
    # tree2 = BST([5,2,3,4,1])
    # print(tree2)
    # print(tree2.remove(2))
    # print(tree2)
    #
    # print("----------Self test 5 remove---------")
    #
    # tree2 = BST([4,2,3,1])
    # print(tree2)
    # print(tree2.remove(2))
    # print(tree2)
    #
    # print("----------Self test 6 remove---------")
    #
    # tree2 = BST([4,6,5,7])
    # print(tree2)
    # print(tree2.remove(6))
    # print(tree2)
    #
    #
    # print("----------Self test 7 remove---------")
    #
    # tree2 = BST([1, 2, 2, 3, 3, 3])
    # print(tree2)
    # print(tree2.remove(2))
    # print(tree2)
    #
    #
    #
    print("----------Self test 8 remove---------")

    tree = BST([8, -2, 5, 3, 0, 2, 8])
    print(tree)
    print(tree.remove(-2))
    print(tree)
   # comment out the following lines
    #if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove_first())
    # print(tree)
    #
    # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    #
    # """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')


    tree = BST([38, 50, 17])
    print(tree)
    tree.remove_first()
    tree.in_order_traversal()
    print(tree.post_order_traversal())
