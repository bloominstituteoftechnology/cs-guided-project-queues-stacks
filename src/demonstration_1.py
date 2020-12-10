"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.
​
You already have a `Stack` class that you've implemented using a dynamic array.
​
Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.
​
*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
​
    def __len__(self):
        return len(self.items)
​
    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
​
    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
​
        return self.items.pop()
​
    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]
​
class MaxStack:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        self.maxes = Stack()
​
    def push(self, item):
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # check to see if our input > our current max 
        if len(self.maxes) == 0 or item > self.maxes.peek():
            self.maxes.push(item)
​
    def pop(self):
        """Remove and return the top item from our stack."""
        # Your code here
        # check our maxes stack to see if the element we're 
        # popping == the current max 
        if len(self.stack) == 0:
            return None
​
        if self.stack.peek() == self.maxes.peek():
            self.maxes.pop()
​
        return self.stack.pop()
​
    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
        """
        Idea 1: Iterate through all of the elements in our stack, find the 
        largest, and return it. O(n) 
​
        Idea 2: Can we make a `self.max` property in the class and 
        modify it as we go? O(1)
        What happens when we pop the max value from our stack? How 
        do we find the next max value that needs to replace it? 
        It's not enough to just store the current max. What we need 
        is the history of all the maxes. This way, when we remove the 
        current max, we know what was the max before it, and we can 
        set that as our current max.
        We'll use another stack specifically to keep track of the 
        history of max values.
        """
        return self.maxes.peek()
​
max_stack = MaxStack()
print(max_stack.get_max()) # returns None
​
max_stack.push(15)
print(max_stack.get_max()) # returns 15
​
max_stack.push(100)
print(max_stack.get_max()) # returns 100
​
max_stack.push(22)
print(max_stack.get_max()) # returns 100
​
print(max_stack.pop()) # returns 22 
print(max_stack.get_max()) # returns 100
​
print(max_stack.pop()) # returns 100
print(max_stack.get_max()) # returns 15