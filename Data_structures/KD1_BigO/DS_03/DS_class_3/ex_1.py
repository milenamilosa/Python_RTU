class Node:
    def __init__(self, value):
        self.value = value  # stores the value of the node
        self.next = None    # points to the next node in the sequence
        
class Queue:                        # represents the queue data structure
    def __init__(self, value):      # takes an initial value and creates a new node with that value
        new_node = Node(value)
        self.first = new_node       # points to the first node in the queue
        self.last = new_node        # points to the last node
        self.length = 1             # keeps track of the number of nodes in the queue

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next




my_queue = Queue(4)

my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""