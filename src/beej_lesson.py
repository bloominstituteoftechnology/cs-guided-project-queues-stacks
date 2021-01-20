class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None
​
    def __repr__(self):
        return f"ListNode({repr(self.value)})"
​
class LinkedList:
    def __init__(self, head=None):
        self.head = head
​
    def __str__(self):
        cur = self.head
        result = ""
​
        while cur is not None:
            result += str(cur.value)
            if cur.next is not None:
                result += " -> "
            cur = cur.next
​
        return result
​
    def add_to_head(self, n):
        # Set next on new node to old head
        n.next = self.head
​
        # Set head of list to new node
        self.head = n
​
    def del_from_head(self):
        if self.head is None:
            return None
​
        old_head = self.head
        self.head = self.head.next
​
        old_head.next = None
​
        return old_head
​
    def find_tail(self):
        if self.head is None:
            return None, None
​
        prev = None
        cur = self.head
​
        while cur.next is not None:
            prev = cur
            cur = cur.next
​
        return (prev, cur)
​
    def push(self, n):
        self.add_to_head(n)
​
    def pop(self):
        return self.del_from_head()
​
    def enqueue(self, n):
        self.add_to_head(n)
​
    def dequeue(self):
        prev, tail = self.find_tail()
        if prev is None:
            # dequeue the head
            self.head = None
        else:
            prev.next = None
        return tail
​
​
​
ll = LinkedList()
ll.enqueue(ListNode(11))
ll.enqueue(ListNode(37))
ll.enqueue(ListNode(5))
ll.enqueue(ListNode(12))
​
print(ll)
​
item = ll.dequeue()
print(item)
item = ll.dequeue()
print(item)
item = ll.dequeue()
print(item)
item = ll.dequeue()
print(item)
item = ll.dequeue()
print(item)
item = ll.dequeue()
print(item)