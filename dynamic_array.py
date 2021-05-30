# Course: CS261 - Data Structures
# Student Name:Jesse Zelaya
# Assignment: Creating Dynamic Array
# Description: Create Dynamic array and methods for it.
# Last revised: October 26th 2020


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        TODO: Write this implementation
        Resize dynamic array to have a new capacity based on
        new capacity parameter, no value returned
        """
        # check if new capacity is greater than current size and is positive
        if new_capacity >= self.size and new_capacity > 0:
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        TODO: Write this implementation
        Adds element to end of array, if end of array reached
        it doubles the array size, no value returned
        """
        # check if array is full and double capacity if that's the case
        # copy array to
        if self.length() < self.capacity:
            self.data[self.size] = value
            self.size += 1
        else:
            self.resize(self.capacity*2)
            new_arr = StaticArray(self.capacity)
            for i in range(0, self.size):
                new_arr[i] = self.data[i]
            self.data = StaticArray(self.capacity)
            # point to new array
            self.data = new_arr
            # for i in range(0, self.capacity):
            #     self.data[i] = new_arr[i]
            self.data[self.size] = value
            self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        Inserts element value into dynamic array at index given
        no value returned
        """
        # assure index not less than 0
        if index < 0 or index > self.length():#.length():
            raise DynamicArrayException

        # check if there is room to insert
        if self.length() <= self.capacity-1:# and index <= self.length()+1:#.length():

            # shift array to the right one element space
            for i in range(0, self.capacity):
                if i < index:
                    pass
                elif i == index:
                    # save current place
                    current = self.data[i]
                    # replace current place with value
                    self.data[i] = value
                    # save next place
                    if i < self.capacity-1:
                        next = self.data[i+1]
                    #replace next place with current place
                        self.data[i+1] = current
                    self.size += 1
                elif i > index:
                    # save current as next
                    current = next
                    # update next
                    if i+1 < self.length():
                        next = self.data[i+1]
                    # shift current to next
                        self.data[i+1] = current

        else:
            self.resize(self.capacity*2)
            new_arr = StaticArray(self.capacity)
            for i in range(0, self.length()):
                new_arr[i] = self.data[i]
            self.data = new_arr
            self.insert_at_index(index, value)



    def get_at_index(self, index: int) -> object:
        """
        TODO: Write this implementation
        returns element at the index given from dynamic array
        """
        # assure index is within range
        if index < 0 or index >= self.length():
            raise DynamicArrayException
        else:
            return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        passes an index and removed the element from that index in the dynamic array
        returns nothing
        """
        # when number of elements before removal
        # is less than 1/4 of the capacity
        # reduce to twice the number of elements AND reduction is not less than 10
        if index < 0 or index > self.length() - 1:
            raise DynamicArrayException

        if self.length() < .25 * self.capacity and self.capacity >= 10:
            if self.length()*2 < 10:
                self.resize(10)
            else:
                self.resize(self.length()*2)

        # update elements except for index, set index to None
        # shift all of the elements after the removed element
        # toward 0
        for i in range(0, self.length()):
            if i < index:
                pass
            elif i == index:
                self.data[i] = None
                # update length of array
                self.size -= 1

            elif i > index:
                self.data[i-1] = self.data[i]
                if i == self.length() - 1:
                    self.data[i] = None



    def slice(self, start_index: int, quantity: int) -> object:
        """
        TODO: Write this implementation
        creates a new dynamic array with values from the elements
        in range between index given and quantity
        returns new array
        """
        # check for valid parameters
        if start_index < 0:
            raise DynamicArrayException
        if (start_index >= self.length()
                or (quantity - start_index) > self.length() - start_index
                or quantity < 0
                or quantity > self.length()-start_index):
                raise DynamicArrayException

        # create new array for slice
        sliced_arr = DynamicArray([])

        # add elements to new slice
        for i in range(0, quantity):
            sliced_arr.append(self.data[start_index+i])
        return sliced_arr

    def merge(self, second_da: object) -> None:
        """
        TODO: Write this implementation
        Merges two arrays together by adding passed array to the end
        of the original array
        nothing returned
        """

        # add second array to the end of original
        for i in range(0, second_da.length()):
            self.append(second_da.get_at_index(i))

    def map(self, map_func) -> object:
        """
        TODO: Write this implementation
        Applies function to values in given array
        and stores elements in new array
        returns array
        """

        # create new array
        arr2 = DynamicArray()

        # apply function outputs to new array
        for i in range(0, self.length()):
           arr2.append(map_func(self.data[i]))
        return arr2

    def filter(self, filter_func) -> object:
        """
        TODO: Write this implementation
        Adds values to new array that are filtered by function condition
        returns new array
        """

        # create new array
        arr2 = DynamicArray()

        # apply function to values in array and append to new
        for i in range(0, self.length()):
            if filter_func(self.data[i]):
                arr2.append(self.data[i])
        return arr2

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        TODO: Write this implementation
        applies reduce_func to elements in array
        if no initializer is supplied then the first
        value is the initial value.
        every value after has function applied
        returns total value of output
        """
        if self.is_empty():
            return initializer
        # if initializer is None then set initial value to the first index
        elif initializer == None:
            initial_value = self.data[0]
            # loop for interating and adding squared values to initial value
            for i in range(1, self.length()):
                initial_value = reduce_func(initial_value, self.get_at_index(i))
            return initial_value

        # Repeat for a sequence with initializer
        elif initializer != None:
            initial_value = initializer
            for i in range(0, self.length()):
                initial_value = reduce_func(initial_value, self.get_at_index(i))
            return initial_value

    def magic(self) -> None:
        for i in range(self.size - 1, -1, -1):
            self.append(self.data[i])
            self.remove_at_index(i)
        return





# BASIC TESTING
if __name__ == "__main__":

    m = DynamicArray([9,3,4,6,2])
    print(m)
    m.magic()
    print(m)

    for i in range(5 - 1, -1, -1):
        print(i)
    #
    # print("\n# resize - example 1")
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.resize(8)
    # print(da.size, da.capacity, da.data)
    # da.resize(2)
    # print(da.size, da.capacity, da.data)
    # da.resize(0)
    # print(da.size, da.capacity, da.data)
    #
    # print("\n# resize - example 2")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)
    #
    # print("\n# append - example 1")
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)
    #
    # print("\n# append - example 2")
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    # print("\n# append - example 3")
    # da = DynamicArray()
    # for i in range(10000):
    #     da.append(i)
    # print(da.size)

    # #
    # print("\n# insert_at_index - example 1")
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)
    #
    # print("\n# insert_at_index example 2")
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised1:", type(e))
    #     da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)
    #
    # print("\n# insert at index example 3")
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Can not insert value", value, "at index", index)
    # print(da)
    #
    # print("\n# get_at_index - example 1")
    # da = DynamicArray([10, 20, 30, 40, 50])
    # print(da)
    # for i in range(4, -1, -1):
    #     print(da.get_at_index(i))
    #
    # print("\n# get_at_index example 2")
    # da = DynamicArray([100, 200, 300, 400, 500])
    # print(da)
    # for i in range(-1, 7):
    #     try:
    #         print("Index", i, ": value", da.get_at_index(i))
    #     except Exception as e:
    #         print("Index", i, ": exception occurred")
    #
    # #
    #
    # print("\n# remove_at_index - example 1")
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # da.remove_at_index(6)
    # da.remove_at_index(2)
    # print(da)
    #
    # print('# remove_at_index - example 2')
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    #     #print(da.size, da.capacity)
    # print(da.size, da.capacity)
    # for i in range(16, -1, -1):
    #     #print(da.size, da.capacity)
    #     #print(i)
    #     da.remove_at_index(0)
    # print(da)
    #
    # print("\n# remove_at_index - example 3")
    # da = DynamicArray()
    # print(da.size, da.capacity)
    # [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 3 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 4 - remove 1 element
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 6 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 7 - remove 1 element
    # print(da.size, da.capacity)
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.size, da.capacity, end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.size, da.capacity)
    #
    #
    # print("\n# remove at index - example 4")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # print(da)
    # for _ in range(5):
    #     da.remove_at_index(0)
    #     print(da)
    #
    #
    #
    # print("\n# slice example 1")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")
    #
    # print("\n# slice example 2")
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOUCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")
    #
    # print("\n# merge example 1")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)
    #
    # print("\n# merge example 2")
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)
    #
    # print("\n# map example 1")
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # print(da.map(lambda x: x ** 2))
    #
    #
    # print("\n# map example 2")
    # def double(value):
    #     return value * 2
    #
    # def square(value):
    #     return value ** 2
    #
    # def cube(value):
    #     return value ** 3
    #
    # def plus_one(value):
    #     return value + 1
    #
    # da = DynamicArray([plus_one, double, square, cube])
    # for value in [1, 10, 20]:
    #     print(da.map(lambda x: x(value)))

    #
    # print("\n# filter example 1")
    # def filter_a(e):
    #     return e > 10
    #
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # result = da.filter(filter_a)
    # print(result)
    # print(da.filter(lambda x: (10 <= x <= 20)))
    #
    #
    # print("\n# filter example 2")
    # def is_long_word(word, length):
    #     return len(word) > length
    #
    # da = DynamicArray("This is a sentence with some long words".split())
    # print(da)
    # for length in [3, 4, 7]:
    #     print(da.filter(lambda word: is_long_word(word, length)))

    #
    # print("\n# reduce example 1")
    # values = [100, 5, 10, 15, 20, 25]
    # da = DynamicArray(values)
    # print(da)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    #
    # print("\n# reduce example 2")
    # da = DynamicArray([100])
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    # da.remove_at_index(0)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))

    #my test conditions
    # d = DynamicArray([2,2,2])
    # print("d arr", d)
    # d.insert_at_index(3,70)
    # print(d,"after insert")