"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxNumber = None


    def push(self, item):
        """Add a new item onto the top of our stack."""
         if self.maxNumber == None or item > self.maxNumber:
            self.maxNumber = item
        self.stack.push(item)


    def pop(self):
        """Remove and return the top item from our stack."""
        return self.stack.pop()


    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxNumber

currStack = MaxStack()

currStack = push(100)
currStack = push(10)
currStack = push(4)
currStack = push(2)
currStack = push(0)
currStack = push(99)

print(currStack.get_max())
