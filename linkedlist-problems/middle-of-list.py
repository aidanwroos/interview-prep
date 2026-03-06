# given head of linked list, return the middle node of the list
# 1. Two Pass approach O(n) time, O(1) space
# 2. Hare and Tortoise approach O(n) time, O(1) space


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

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    #Two Pass approach O(n) time, O(1) space
    def middleOfList(self):
        list_len = self.get_length(self.head)
        
        i = 0
        current = self.head
        while i < list_len // 2:
            current = current.next
            i += 1

        print(f"{current.data}")

    #The Hare and Tortoise approach O(n) time, O(1) space
    def hareAndTortoise(self):
        
        #initialize slow and fast pointers to begin at the head
        slowptr = self.head
        fastptr = self.head;
        
        #while fastptr hasn't reached the end of the list (None)
        while fastptr:
            slowptr = slowptr.next       #increment by 1
            fastptr = fastptr.next.next  #increment by 2

        #slowptr should be at middle of list now, print its data
        print(f"{slowptr.data}")



ll = LinkedList()
for i in range(10):
    ll.append(i)

ll.display()
ll.middleOfList()
ll.hareAndTortoise()