#delete the middle node of a linked list

from classes import LinkedList, Node

#two pass approach O(n) time, O(1) space
def deleteMiddle(ll):
    list_len = ll.get_length()

    i = 0
    current = ll.head
    prev = None

    while i < list_len // 2:
        next_node = current.next
        prev = current
        current = next_node
        i += 1
    
    #skip middle element by resetting the pointer to
    #point to next node
    prev.next = current.next
    



ll = LinkedList()
for i in range(10):
    ll.append(i)

#deleted node is 5
print(f"{ll.display()}")
deleteMiddle(ll)
print(f"{ll.display()}")