"""Using Adapter pattern - it is a design pattern that
involves modifying the method of an existing class or interface
to look like that of the methods of a similar class or interface
"""

# create an appropriate class to raise an appropriate message
# for an empty stack as against the index error raised by List
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class DoubleStack:
    """LIFO Stack implementation usig a python List
    to create a double stack peculiar to 2 colours red
    and blue

    red stack will and blue stack will converge towards
    center of the array
    """

    def __init__(self, size=10):
        """Create an inital stack with size"""
        self._data = [None] * size
        self._red_index = 0
        self._blue_index = size - 1

    def __len__(self):
        """Returns the len of the elements in the list"""
        return len(self._data)

    def __str__(self):
        """Return the string representation of the data"""
        a = ''
        count_empty_slot = 0

        for i in range(len(self._data)):
            if self._data[i] is None:
                a += ' | |'
                count_empty_slot += 1
            else:
                a += ' |{0}|'.format(str(self._data[i]))
        top =  'red stack -->'
        bottom = '\t' * len(self._data) + '<-- blue stack'
        return top + '\n' + ('\t' * 2) + a + "\n" + bottom + '\n\n' + \
            'no of empty slot: {0}'.format(str(count_empty_slot))

    def _resize(self, capacity):
        """Resize the list to a capacity"""
        old_stack = self._data                                       # hold the existing stack
        initial_blue_index = self._blue_index
        self._data = [None] * capacity                               # allocate a new list/stack
        data_size_difference = len(self._data) - len(old_stack)
        self._blue_index = initial_blue_index + data_size_difference  # reset the the blue_index

        for i in range(self._red_index):                               # copy the data in old stack to the new allocated array
            self._data[i] = old_stack[i]

        for j in range(self._blue_index, len(self._data)):
            self._data[j] = old_stack[j - data_size_difference]

    def push_red(self, val):
        """Add the val to the top of the red (left)stack"""
        if len(self._data) <= (self._red_index + (len(self._data) - 1 - self._blue_index)):
            self._resize(len(self._data) * 2)     # increase the capacity by 2 initial size

        self._data[self._red_index] = val
        self._red_index += 1

    def pop_red(self):
        """Remove and return the last element on the left stack"""
        val = self.top_red()                        # get the top value
        self._data[self._red_index - 1] = None          # Assign the slot empty
        self._red_index -= 1                        # the size of red stack is reduced by 1

        return val

    def top_red(self):
        """Get the element at the top of the left/red stack"""
        index = 0 if self._red_index - 1 < 0 else self._red_index - 1

        return self._data[index]

    def push_blue(self, val):
        """Add the val to the top of the blue (right)stack"""
        if len(self._data) <= (self._red_index + (len(self._data) - 1 - self._blue_index)):
            self._resize(len(self._data) * 2)               # increase the capacity by 2 initial size

        self._data[self._blue_index] = val
        self._blue_index -= 1



    def pop_blue(self):
        """Remove and return the last element on the right stack"""
        val = self.top_blue()                               # get the top value

        if val:
          self._data[self._blue_index + 1] = None          # Assign the slot empty
          self._blue_index += 1                             # the index of blue stack is increased by 1

        return val

    def top_blue(self):
        """Get the element at the top of the blue/right stack"""
        print(self._blue_index, len(self._data))
        if self._blue_index == self._red_index or self._blue_index + 1 >= len(self._data):
            return None

        return self._data[self._blue_index + 1]




stack = DoubleStack(size=4)
stack.push_red(56)
stack.push_red('bahy')
stack.pop_red()
stack.pop_red()
stack.push_red(56)
stack.push_red('bahy')
stack.push_red('bahy')
stack.push_red('myBBY')
stack.push_red('heealthy')
stack.push_red('heealthy food')
stack.push_blue('blue heealthy food')
stack.push_blue('blue food')
stack.push_blue('blue')
stack.push_red('red 1')
stack.pop_blue()
stack.pop_blue()
stack.pop_blue()
stack.pop_blue()
stack.push_blue('blue')
print(stack.top_red())
print(stack.top_blue())
print(stack)
