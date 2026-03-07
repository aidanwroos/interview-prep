#reverse a linked list by its nodes, (not by its values)

from classes import LinkedList, Node


#iterative method O(n) time, O(1) space
def reverseList(ll):

    current = ll.head
    prev = None

    while current is not None:

        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    
    # after breaking, current is now None, 
    # meaning prev is the last node. Set head to it.
    ll.head = prev



ll = LinkedList()
for i in range(10):
    ll.append(i)
    
print(f"Original: {ll.display()}")
reverseList(ll)
print(f"Reversed: {ll.display()}")




    