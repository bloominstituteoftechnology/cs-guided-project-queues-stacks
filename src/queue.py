class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
​
class Queue:
    def __init__(self):
        # reference to the head of our linked list 
        self.head = None
        # reference to the tail of our linked list 
        self.tail = None
​
    def enqueue(self, val):
        new_node = Node(val)
        # check if our queue is empty 
        if self.head is None and self.tail is None:
            self.head = new_node  
            self.tail = new_node
        # adds the val to one of the queue 
        else:
            # connect the old tail to the new node 
            self.tail.next = new_node
            # update the tail reference to refer to 
            # the new node 
            self.tail = new_node
​
    def dequeue(self):
        # check if the our queue is empty
        if self.head is None and self.tail is None:
            return None
        # check is the queue only has one element
        if self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.val
        # removes a val from the opposite end 
        # in which the element was added 
        else:
            old_head = self.head 
            self.head = self.head.next
            return old_head.val
    
queue = Queue()
​
queue.enqueue(15)
queue.enqueue(22)
queue.enqueue(27)
​
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())