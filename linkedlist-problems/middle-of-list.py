# given head of linked list, return the middle node of the list

from classes import LinkedList, Node


#Two Pass approach O(n) time, O(1) space
def twoPass(ll):
    i = 0
    list_len = ll.get_length()
    current = ll.head

    while i < list_len // 2:
        current = current.next
        i += 1

    return current.data


#The Hare and Tortoise approach O(n) time, O(1) space
def hareAndTortoise(ll):
    #initialize slow and fast pointers to begin at the head
    slowptr = ll.head
    fastptr = ll.head
    
    #while fastptr hasn't reached the end of the list (None)
    while fastptr and fastptr.next:
        slowptr = slowptr.next       #increment by 1
        fastptr = fastptr.next.next  #increment by 2

    #slowptr should be at middle of list now, print its data
    return slowptr.data



ll = LinkedList()
for i in range(10):
    ll.append(i)

print(f"{ll.display()}")
print(f"{twoPass(ll)}")
print(f"{hareAndTortoise(ll)}")