# Course: CS261 - Data Structures
# Student Name: Jesse Zelaya
# Assignment:   Bag Asssignment
# Description:  Uses dynamic array to
# Last revised: October 26, 2020

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        Adds value/element to the bag by appending to DA
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:

        """
        removes element from the bag
        :param value: element to remove
        :return: true if removed, false if not found
        """
        # check each element in array and remove that index value
        N_len = self.da.length()
        for i in range(0, N_len):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        counts the number of an element given
        :param value: element to count
        :return: returns count
        """
        N_len = self.da.length()
        val_count = 0

        # iterate and count elements in bag
        for i in range(0, N_len):
            if self.da.get_at_index(i) == value:
                val_count += 1
        return val_count

    def clear(self) -> None:
        """
        clears the entire bag
        :return: nothing returned, bag altered
        """
        N_len = self.da.length()
        # iterate through to remove each index 0 element
        for i in range(0, N_len):
            self.da.remove_at_index(0)

    def equal(self, second_bag: object) -> bool:
        """
        checks if bags are equal to eachother
        :param second_bag: bag to compare to current
        :return: returns true if equal false if not
        """
        if self.size() == 0 and 0 == second_bag.size():
            return True

        N_len = self.da.length()
        M_len = second_bag.da.length()

        # compare elements in both bags
        if self.size() != second_bag.size():
            return False
        else:
            for i in range(0, N_len):
                if self.count(self.da.get_at_index(i)) != second_bag.count(self.da.get_at_index(i)):
                    return False
            return True



# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
