class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:        # checks if the queue is empty
            return None             # operation cannot be performed on an empty queue
        temp = self.first           # stores a reference to the current first node
        if self.length == 1:
            self.first = None       # pointers are set to None to indicate an empty queue
            self.last = None
        else:
            self.first = self.first.next    # updates pointer to point to the next node in the queue
            temp.next = None                #  removes the reference from the dequeued node to the next node
        self.length -= 1            # decremented by one to reflect the removal of an element from the queue
        return temp                 # the method returns the dequeued node stored in the temp variable

 

 
my_queue = Queue(1)
my_queue.enqueue(2)
# my_queue.enqueue(3)

my_queue.print_queue()

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""