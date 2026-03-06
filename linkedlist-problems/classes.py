#main LinkedList and Node classes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #ptr to next node
    
class LinkedList:
    def __init__(self):
        self.head = None #start w/ empty list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def get_length(self):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        return length